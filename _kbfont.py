import sqlite3, datetime, os
ROOT = r"C:\Users\SCC1202201146\Documents\Ngoding\math-hero"
c = sqlite3.connect(os.path.join(ROOT, "kb.sqlite"))
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
c.execute("INSERT INTO log_kerja (waktu, agent, tahap, aktivitas, status, catatan) VALUES (?,?,?,?,?,?)", (now, "zeke", "T7",
  "Keterbacaan teks: font Pixelzone (public/assets/pixelzone-font, CC0) dipasang di CSS (@font-face) untuk semua layar, dan di canvas. Teks canvas (nama boss, nama jembatan, prompt, label aksi, pesan, HUD, jeda, angka pilihan) memakai bubble krem bergaris ungu via helper bubbleText(). Ukuran font dinaikkan dan dibuat kelipatan 8. HUD: ikon hati diganti teks 'Nyawa: n' karena glyph hati tidak ada di font pixel. Tombol aksi 24px.",
  "selesai",
  "Verifikasi: document.fonts.check OK, tanpa error JavaScript, screenshot tests/screenshot-teks-bubble-menara.png dan screenshot-teks-bubble-hutan.png. Keputusan pengguna: level 1-4 tetap kerajaan awan dengan adaptasi craftpix; level 5-8 baru; knockback diterima; skala 2x diterima; hero bisa dipilih; level dibuat ulang; latar terserah zeke; tiny-hero diekstrak. Fase 1 (mesin) belum dimulai."))
c.commit()
os.remove(os.path.join(ROOT, "_fontcheck.py"))
print("ok", now)
