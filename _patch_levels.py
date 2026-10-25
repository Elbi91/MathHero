import io
p = 'public/js/levels.js'
s = io.open(p, encoding='utf-8', newline='').read()

# Tambahan DSL: isle (pulau setinggi k sampai dasar) dan ceil (langit-langit gua).
s = s.replace("  // Hapus tanah (jurang)", """  // Pulau padat dengan permukaan setinggi k (boleh negatif), turun sampai dasar level.
  P.isle = function (c0, c1, k) {
    for (let c = c0; c <= c1; c++) for (let r = this.R - k; r < this.rows; r++) this.set(c, r, 1);
  };
  // Langit-langit gua: n baris padat dari atas.
  P.ceil = function (c0, c1, n) {
    for (let c = c0; c <= c1; c++) for (let r = 0; r < n; r++) this.set(c, r, 1);
  };
  // Hapus tanah (jurang)""")

a = s.index('  const LEVELS = [level1()];')
more = r'''  // ---------- LEVEL 2: Hutan Pelangi (bukit, lebah kotak, papan rapuh, jembatan, platform gerak, bos naga) ----------
  function level2() {
    const b = new Builder({
      id: 2, cols: 134, rows: 28, nama: 'Hutan Pelangi', tema: 'grassB', bg: 'forest', waktu: 'maghrib', lv: 2, musik: 'maghrib',
      cerita: ['Jembatan pelangi di hutan itu rusak.', 'Naga Kabut menjaga ujung hutan!'],
    });
    b.ground(0, 46);
    b.put(3, 0, 'S');
    b.row(7, 9, 0, '*');
    b.block(11, 1, 3, 1); b.block(14, 2, 3, 2); b.block(17, 3, 3, 3); b.block(20, 2, 3, 2);
    b.put(12, 1, '*'); b.put(15, 2, '*'); b.put(18, 3, '*');
    b.put(24, 0, '?', { op: 'add', lv: 2 });
    b.put(27, 0, 'c');
    b.hint(29, 0, 'Lebah kotak terbang bolak-balik!');
    b.put(32, 2, 'f', { range: 3 });
    b.put(35, 0, 'b');
    b.plat(37, 3, 3); b.plat(41, 5, 3); b.plat(45, 7, 3);
    b.put(38, 3, '*'); b.put(42, 5, '*'); b.put(46, 7, '$');
    b.put(40, 0, '^'); b.put(41, 0, '^');
    b.put(44, 0, '?', { op: 'mul', lv: 2 });
    b.hint(45, 0, 'Papan rapuh jatuh. Lari terus!');
    b.crumble(47, 0, 4);
    b.ground(51, 78);
    b.put(55, 0, 'a'); b.put(58, 0, 'h'); b.put(60, 0, 'b', { dir: 1 }); b.put(64, 2, 'f', { range: 2.5 });
    b.hint(66, 0, 'Pecahkan tumpukan peti dengan soal');
    b.gate(69, 0, 3, { op: 'mul', lv: 2 });
    b.put(73, 0, 'c');
    b.put(76, 0, '?', { op: 'add', lv: 2 });
    b.hint(77, 0, 'Jawab soal untuk memasang jembatan');
    b.bridge(79, 0, 10, { parts: 3, op: 'susun', lv: 2, nama: 'Jembatan Pelangi' });
    b.ground(89, 106);
    b.put(92, 0, 'a'); b.put(97, 2, 'f', { range: 3 }); b.put(101, 0, 'b');
    b.hint(104, 0, 'Naiki platform yang bergerak');
    b.mover(109, 0, 3, { axis: 'x', range: 1.5, speed: 0.2 });
    b.ground(114, 133);
    b.put(116, 0, 'c');
    b.put(119, 0, '?', { op: 'mul', lv: 2 });
    b.hint(121, 0, 'Naga Kabut ada di depan!');
    b.boss(128, 0, { kind: 'dino', nama: 'Naga Kabut', hp: 3, a0: 122, op: 'mul', lv: 2 });
    b.put(132, 0, 'E');
    b.deko(14, 4, 'bee', 30, { bob: true }); b.deko(30, 0, 'strawberry', 34); b.deko(52, 0, 'pineapple', 52);
    b.deko(67, 0, 'chick', 34, { bob: true }); b.deko(98, 0, 'banana', 40); b.deko(113, 5, 'bee', 30, { bob: true });
    return b.build();
  }

  // ---------- LEVEL 3: Pulau Permen (pulau melayang, laut platform gerak, tong penyeruduk, pilih jawaban) ----------
  function level3() {
    const b = new Builder({
      id: 3, cols: 150, rows: 28, nama: 'Pulau Permen', tema: 'candy', bg: 'candy', waktu: 'siang', lv: 3, musik: 'permen',
      cerita: ['Raja Permen ingin pulaunya manis lagi.', 'Lompati pulau-pulau permen!'],
    });
    b.isle(0, 13, 0); b.put(3, 0, 'S'); b.row(7, 9, 0, '*');
    b.isle(17, 29, 0);
    b.put(19, 1, '*'); b.put(20, 0, '?', { op: 'add', lv: 3 }); b.put(24, 0, 'b');
    b.isle(33, 44, 2);
    b.put(34, 2, 'c'); b.put(38, 2, 'a');
    b.plat(40, 5, 3); b.put(41, 5, '*'); b.plat(36, 5, 3); b.put(37, 5, '*');
    b.isle(48, 56, 0);
    b.put(52, 3, 'f', { range: 2 });
    b.put(54, 0, '?', { op: 'mul', lv: 3 });
    b.hint(55, 0, 'Naiki platform gerak. Jangan jatuh!');
    b.mover(59, 0, 3, { axis: 'x', range: 1.5, speed: 0.18 });
    b.mover(65, 0, 3, { axis: 'x', range: 2, speed: 0.18, phase: 0.5 });
    b.mover(72, 0, 3, { axis: 'x', range: 1.5, speed: 0.18 });
    b.put(61, 3, '*'); b.put(67, 3, '*'); b.put(74, 3, '*');
    b.isle(77, 100, 0);
    b.put(78, 0, 'c');
    b.hint(81, 0, 'Pecahkan peti: pembagian!');
    b.gate(84, 0, 3, { op: 'div', lv: 3 });
    b.put(88, 0, 'r'); b.put(93, 3, 'f', { range: 2.5 });
    b.put(96, 0, '?', { op: 'div', lv: 3 });
    b.isle(104, 149, 0);
    b.put(105, 0, 'c');
    b.block(108, 1, 2, 1); b.block(110, 2, 2, 2); b.block(112, 3, 2, 3); b.block(114, 4, 2, 4);
    b.put(108, 1, '*'); b.put(110, 2, '*'); b.put(112, 3, '*'); b.put(114, 4, '*');
    b.plat(118, 6, 3); b.put(119, 6, '$');
    b.put(121, 0, '?', { op: 'mul', lv: 3 });
    b.hint(123, 0, 'Pilih platform dengan jawaban yang benar');
    b.pilih([125, 129, 133], 3, { op: 'add', lv: 3 });
    b.put(120, 0, 'a'); b.put(137, 0, 'r'); b.put(139, 0, 'c'); b.put(142, 0, 'h');
    b.put(146, 0, 'E');
    b.deko(10, 0, 'lollipop', 80); b.deko(30, 0, 'candy', 34); b.deko(46, 2, 'cherry', 40); b.deko(50, 0, 'watermelon', 50);
    b.deko(90, 0, 'lollipop', 90); b.deko(116, 0, 'candy', 34); b.deko(144, 0, 'lollipop', 80);
    return b.build();
  }

  // ---------- LEVEL 4: Menara Awan (menara tegak, platform tembus, bos robot di puncak) ----------
  function level4() {
    const b = new Builder({
      id: 4, cols: 13, rows: 62, nama: 'Menara Awan', tema: 'stone', bg: 'sky', waktu: 'malam', lv: 4, musik: 'awan',
      cerita: ['Menara Awan menjulang sampai ke langit.', 'Naiklah terus. Hati-hati dengan robot di puncak!'],
    });
    b.isle(0, 12, 0);
    b.put(6, 0, 'S');
    b.hint(3, 0, 'Naik! Platform bisa ditembus dari bawah');
    b.hint(9, 0, 'Turun: geser bawah + lompat');
    for (let i = 1; i <= 15; i++) {
      const k = 3 * i, left = i % 2 === 1;
      if (i === 7) { b.mover(2, k, 3, { axis: 'x', range: 1.5, speed: 0.2 }); continue; }
      if (i === 10) { b.crumble(7, k, 6); b.put(9, k, '*'); continue; }
      if (left) { b.plat(0, k, 5); b.put(1, k, '*'); } else { b.plat(7, k, 6); b.put(11, k, '*'); }
    }
    b.put(9, 6, '?', { op: 'add', lv: 4 });
    b.put(2, 9, 'c');
    b.put(2, 15, '?', { op: 'mul', lv: 4 });
    b.put(3, 24, 'f', { range: 1.5 });
    b.put(11, 18, 'a', { dir: -1 });
    b.put(10, 24, 'c');
    b.put(2, 27, '?', { op: 'div', lv: 4 });
    b.put(0, 33, 'N', { phase: 1.5 });
    b.put(9, 36, '?', { op: 'mul', lv: 4 });
    b.put(1, 39, '^'); b.put(3, 39, '^');
    b.put(2, 42, 'h'); b.put(8, 45, '$');
    b.plat(0, 48, 13);
    b.put(11, 48, 'c');
    b.boss(10, 48, { kind: 'robot', nama: 'Raksasa Menara', hp: 3, a0: 0, ty: (b.R - 48) * T + 6, noWall: true, op: 'div', lv: 4 });
    b.put(1, 48, 'E');
    b.deko(8, 0, 'bee', 28, { bob: true });
    return b.build();
  }

  const LEVELS = [level1(), level2(), level3(), level4()];'''
s = s[:a] + more + s[a + len('  const LEVELS = [level1()];'):]
io.open(p, 'w', encoding='utf-8', newline='').write(s)

# entities: syarat pemicu bos (ty) dan tanpa dinding (noWall); gergaji skala 1
p = 'public/js/entities.js'
e = io.open(p, encoding='utf-8', newline='').read()
e = e.replace("""        if (px > B.a0 * T + 96) {
          W.arenaWall = { x: B.a0 * T, y: 0, w: T, h: L.height, ow: false, wall: true };""", """        const trig = B.def.ty !== undefined ? (P.y + P.h <= B.def.ty && P.onGround) : px > B.a0 * T + 96;
        if (trig) {
          W.arenaWall = B.def.noWall ? null : { x: B.a0 * T, y: 0, w: T, h: L.height, ow: false, wall: true };""")
e = e.replace("sp(ctx, 'trap2', Math.floor(s.ang) % 7, s.cx - cx, s.y + 16 - cy, S, false);", "sp(ctx, 'trap2', Math.floor(s.ang) % 7, s.cx - cx, s.y + 16 - cy, 1, false);")
io.open(p, 'w', encoding='utf-8', newline='').write(e)
print('ok')
