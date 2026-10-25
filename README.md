# Math Hero

Game petualangan matematika untuk anak kelas 1 sampai 3 SD. Dimainkan di Chrome Android lewat jaringan lokal (hotspot HP), jadi tidak perlu internet saat bermain.

## Cara menjalankan

1. Pastikan laptop dan HP terhubung ke hotspot yang sama. Nyalakan hotspot di HP, lalu sambungkan laptop ke hotspot itu.
2. Klik 2x `run.bat` di folder project.
   - Pertama kali, skrip memeriksa Node.js. Jika belum ada, skrip memasangnya lewat winget. Jika pemasangan selesai, tutup jendela, lalu klik 2x `run.bat` lagi.
   - Jendela akan menampilkan alamat seperti `http://10.x.x.x:8091`. Itu alamat untuk HP.
3. Di HP, buka Chrome dan ketik alamat itu. Jangan pakai `localhost` di HP, karena itu mengarah ke HP sendiri.
4. Untuk menghentikan server, tutup jendela `run.bat` atau tekan Ctrl+C di jendela itu.

Kalau alamat IP laptop berubah (misalnya setelah hotspot dimatikan dan dinyalakan lagi), jalankan `ipconfig` di laptop dan cari IPv4 Address pada adapter Wi-Fi atau hotspot. Pakai angka itu di HP.

### Firewall Windows

Saat pertama kali server berjalan, Windows bisa menampilkan peringatan firewall. Izinkan akses untuk jaringan **Private**. Jika terlanjur menolak, buka PowerShell sebagai administrator lalu jalankan:

```
netsh advfirewall firewall add rule name="Math Hero" dir=in action=allow protocol=TCP localport=8091
```

Jika server dijalankan dengan port lain, ganti `8091` sesuai port yang tampil di jendela.

## Kontrol

- **Joystick** (kiri bawah): jalan ke kiri dan kanan.
- **Lompat** (kanan bawah).
- **Aksi** (di samping Lompat): ambil item, buka pintu atau peti, menyerang boss. Tekan dekat objek yang bisa dibuka.
- **Jeda** (kanan atas): berhenti sejenak. Tekan lagi untuk lanjut.
- **Senyap / Bersuara** (sebelah kiri Jeda): mematikan atau menyalakan suara dan musik.

## Aturan permainan

- Health mulai dari 100. Setiap kali health habis, nyawa berkurang 1 dan pemain kembali ke awal area dengan health penuh.
- Pemain punya 3 nyawa. Saat nyawa habis, permainan berakhir dan skor dicatat.
- Semua soal matematika berbentuk pilihan ganda. Tidak ada keyboard.
- Jawaban salah tidak membuat pemain terhukum. Penjelasan langkah akan muncul, dan kamu boleh mencoba lagi.

## Menu utama

- **Mulai Baru**: pilih nama dari daftar, lalu main dari Level 1.
- **Lanjutkan**: pilih pemain yang punya checkpoint. Permainan dimulai dari area terakhir yang dicapai, dengan skor yang sama. Nyawa kembali ke 3.
- **Skor Tertinggi**: 10 skor terbaik dari database.

Setelah kalah atau menamatkan Level 3, permainan kembali ke menu utama.

## Penyimpanan data

Data tersimpan di `data/mathhero.sqlite` (SQLite) di dalam folder project. Isinya:
- nama panggilan dari daftar tetap dan avatar,
- skor dan hasil (kalah atau tamat),
- checkpoint untuk fitur Lanjutkan.

Tidak ada data pribadi yang disimpan. Nama dipilih dari daftar, bukan diketik.

Untuk menghapus semua data, tutup server lalu hapus file `data/mathhero.sqlite`.

## Troubleshooting

- **Halaman tidak terbuka di HP**: pastikan HP dan laptop di hotspot yang sama, alamat IP benar (bukan `localhost`), dan firewall mengizinkan port 8091.
- **Alamat IP tidak muncul di jendela**: jalankan `ipconfig` di laptop dan cari IPv4 Address.
- **Suara tidak terdengar**: buka Chrome, sentuh tombol Mulai terlebih dahulu. Browser mobile baru mengizinkan suara setelah interaksi pertama. Tombol bertuliskan "Senyap" berarti suara sedang menyala (ketuk untuk mematikan). Jika tertulis "Bersuara", suara sedang dimatikan. Pastikan juga volume HP tidak nol.
- **Skor Tertinggi atau Lanjutkan tidak berfungsi**: server mungkin belum berjalan lewat `run.bat`, atau laptop memakai server lain. Tutup semua jendela server lalu jalankan `run.bat` lagi.
- **Layar terasa terpotong atau tombol tertutup**: coba putar HP ke arah lain. Layout sudah diuji dalam mode potret di ukuran layar mirip HP Android, tetapi belum diuji di HP fisik (lihat catatan uji di bagian pengembang).
- **Lag di HP lama**: tutup aplikasi lain di HP. Jika masih lambat, catat HP dan kecepatan fps yang tampil di pojok kiri bawah, lalu laporkan.

## Untuk pengembang

Struktur singkat:
- `server.js`: server statis dan routing API.
- `lib/store.js`: database SQLite dan endpoint API.
- `public/index.html`, `public/css/style.css`: tampilan.
- `public/js/`: `input.js` (kontrol sentuh), `levels.js` (data area), `math.js` (soal), `quiz.js` (panel soal), `audio.js` (suara), `menu.js` (menu utama), `main.js` (gameplay).
- `tests/`: tes otomatis dengan Playwright (Python) dan Node.

Untuk menjalankan tes, siapkan Python dan Playwright:

```
pip install playwright
python -m playwright install chromium
```

Lalu dari folder project:

```
python tests/menu_t8.py
python tests/audio_t7.py
python tests/gameplay_t3.py
node tests/math.test.js
```

Tes Playwright menjalankan server sendiri di port khusus, jadi tidak bentrok dengan server yang sedang berjalan.

Catatan: tes otomatis berjalan di Chromium headless dengan profil Pixel 5. Uji di HP fisik tetap diperlukan untuk memastikan sentuhan, suara, dan performa di perangkat sungguhan.
