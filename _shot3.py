import os, subprocess, time
from playwright.sync_api import sync_playwright
ROOT = r"C:\Users\SCC1202201146\Documents\Ngoding\math-hero"
env = dict(os.environ, PORT="8109")
proc = subprocess.Popen(["node", "server.js"], cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
deadline = time.time() + 10
while time.time() < deadline:
    if "berjalan" in proc.stdout.readline():
        break
errs = []
try:
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(**p.devices["Pixel 5"])
        pg = ctx.new_page()
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto("http://127.0.0.1:8109/")
        time.sleep(1.0)
        pg.evaluate("() => window.__mathHero.startGame(1, 0)")
        time.sleep(4.5)
        pg.evaluate("() => { const m = window.__mathHero; m.player.x = 1500; m.player.y = m.groundY - 44; m.player.vx = 0; }")
        time.sleep(0.6)
        pg.screenshot(path=os.path.join(ROOT, "tests", "screenshot-font-kecil.png"))
        b.close()
finally:
    proc.kill()
os.remove(os.path.join(ROOT, "_shot3.py")) if False else None
print("errors:", errs or "none")
