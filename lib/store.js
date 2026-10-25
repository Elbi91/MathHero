// Penyimpanan Math Hero: pemain, skor, dan progres "Lanjutkan" di SQLite (data/mathhero.sqlite).
// Memakai modul bawaan node:sqlite (Node 22.13+), jadi tidak ada paket npm yang perlu diinstal.
// Data yang disimpan hanya nama panggilan dari daftar tetap dan avatar. Tidak ada data pribadi anak.
const fs = require('fs');
const path = require('path');
const { DatabaseSync } = require('node:sqlite');

const DATA_DIR = path.join(__dirname, '..', 'data');
fs.mkdirSync(DATA_DIR, { recursive: true });
const db = new DatabaseSync(path.join(DATA_DIR, 'mathhero.sqlite'));

db.exec(`
  PRAGMA foreign_keys = ON;
  CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL UNIQUE,
    avatar TEXT NOT NULL,
    dibuat TEXT NOT NULL
  );
  CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL REFERENCES players(id),
    skor INTEGER NOT NULL,
    area INTEGER NOT NULL,
    hasil TEXT NOT NULL,
    waktu TEXT NOT NULL
  );
  CREATE TABLE IF NOT EXISTS progress (
    player_id INTEGER PRIMARY KEY REFERENCES players(id),
    area INTEGER NOT NULL,
    skor INTEGER NOT NULL,
    diperbarui TEXT NOT NULL
  );
`);

// Daftar tetap: anak memilih dengan ketuk, tidak perlu mengetik nama.
const NAMES = ['Bintang', 'Awan', 'Pelangi', 'Kelinci', 'Bulan', 'Kupu-kupu'];
const AVATARS = ['🌟', '☁️', '🌈', '🐰', '🌙', '🦋'];

function now() {
  return new Date().toISOString();
}

function listPlayers() {
  return db.prepare(`
    SELECT p.id, p.nama, p.avatar, (pr.player_id IS NOT NULL) AS punya_progres, pr.area AS area_progres
    FROM players p LEFT JOIN progress pr ON pr.player_id = p.id
    ORDER BY p.id`).all();
}

function getOrCreatePlayer(nama) {
  if (!NAMES.includes(nama)) throw new Error('nama tidak dikenal');
  const avatar = AVATARS[NAMES.indexOf(nama)];
  db.prepare('INSERT OR IGNORE INTO players(nama, avatar, dibuat) VALUES(?,?,?)').run(nama, avatar, now());
  return db.prepare('SELECT id, nama, avatar FROM players WHERE nama = ?').get(nama);
}

function topScores(limit) {
  return db.prepare(`
    SELECT p.nama, p.avatar, s.skor, s.area, s.hasil, s.waktu
    FROM scores s JOIN players p ON p.id = s.player_id
    ORDER BY s.skor DESC, s.waktu ASC LIMIT ?`).all(limit || 10);
}

function addScore(playerId, skor, area, hasil) {
  db.prepare('INSERT INTO scores(player_id, skor, area, hasil, waktu) VALUES(?,?,?,?,?)')
    .run(playerId, Math.max(0, Math.floor(skor)), area, hasil, now());
}

function getProgress(playerId) {
  return db.prepare('SELECT area, skor, diperbarui FROM progress WHERE player_id = ?').get(playerId) || null;
}

function saveProgress(playerId, area, skor) {
  db.prepare(`INSERT INTO progress(player_id, area, skor, diperbarui) VALUES(?,?,?,?)
    ON CONFLICT(player_id) DO UPDATE SET area = excluded.area, skor = excluded.skor, diperbarui = excluded.diperbarui`)
    .run(playerId, area, Math.max(0, Math.floor(skor)), now());
}

function clearProgress(playerId) {
  db.prepare('DELETE FROM progress WHERE player_id = ?').run(playerId);
}

// ---- Endpoint API ----
function send(res, status, body) {
  res.writeHead(status, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' });
  res.end(JSON.stringify(body));
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    let data = '';
    req.on('data', (c) => { data += c; if (data.length > 10000) req.destroy(); });
    req.on('end', () => { try { resolve(data ? JSON.parse(data) : {}); } catch (e) { reject(e); } });
    req.on('error', reject);
  });
}

// Mengembalikan true jika permintaan ditangani di sini.
async function handleApi(req, res, urlPath) {
  if (!urlPath.startsWith('/api/')) return false;
  try {
    if (req.method === 'GET' && urlPath === '/api/players') {
      send(res, 200, { players: listPlayers(), names: NAMES.map((n, i) => ({ nama: n, avatar: AVATARS[i] })) });
      return true;
    }
    if (req.method === 'POST' && urlPath === '/api/players') {
      const b = await readBody(req);
      send(res, 200, { player: getOrCreatePlayer(String(b.nama || '')) });
      return true;
    }
    if (req.method === 'GET' && urlPath === '/api/highscores') {
      send(res, 200, { scores: topScores(10) });
      return true;
    }
    if (req.method === 'POST' && urlPath === '/api/scores') {
      const b = await readBody(req);
      addScore(Number(b.playerId), Number(b.skor) || 0, Number(b.area) || 1, b.hasil === 'tamat' ? 'tamat' : 'kalah');
      send(res, 200, { ok: true });
      return true;
    }
    const m = urlPath.match(/^\/api\/progress\/(\d+)$/);
    if (m) {
      const id = Number(m[1]);
      if (req.method === 'GET') { send(res, 200, { progress: getProgress(id) }); return true; }
      if (req.method === 'PUT') {
        const b = await readBody(req);
        saveProgress(id, Number(b.area) || 1, Number(b.skor) || 0);
        send(res, 200, { ok: true });
        return true;
      }
      if (req.method === 'DELETE') { clearProgress(id); send(res, 200, { ok: true }); return true; }
    }
    send(res, 404, { error: 'tidak ditemukan' });
    return true;
  } catch (e) {
    send(res, 400, { error: String(e.message || e) });
    return true;
  }
}

module.exports = { handleApi, NAMES, AVATARS };
