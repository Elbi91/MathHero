import os
from PIL import Image
B = r"C:\Users\SCC1202201146\Documents\Ngoding\math-hero\public\assets\svg\craftpix\craftpix-net-396765-free-simple-platformer-game-kit-pixel-art"
OUT = r"C:\Users\SCC1202201146\Documents\Ngoding\math-hero\_sheet_out"
os.makedirs(OUT, exist_ok=True)

def info(rel):
    im = Image.open(os.path.join(B, rel)); return rel, im.size

for rel in ["7 Levels/Tiled/Tileset.png", "2 Locations/Backgrounds/1.png", "1 Main Characters/1/Idle.png", "1 Main Characters/1/Run.png",
            "1 Main Characters/1/Hit.png", "1 Main Characters/1/Jump.png", "1 Main Characters/1/Fall.png", "3 Objects/Gems/1.png",
            "3 Objects/Boxes/1_Idle.png", "3 Objects/Boxes/1_Hit.png", "3 Objects/Boxes/1_Break.png", "3 Objects/Checkpoints/Checkpoint_Flag_Idle1.png",
            "3 Objects/Checkpoints/Checkpoint_No_Flag.png", "3 Objects/Checkpoints/End_Idle.png", "3 Objects/Checkpoints/Pointer_Idle.png",
            "4 Enemies/1/Run.png", "4 Enemies/1/Idle.png", "4 Enemies/2/Run.png", "4 Enemies/3/Walk.png", "4 Enemies/3/Charge.png",
            "4 Enemies/4/Walk.png", "4 Enemies/4/Attack.png", "4 Enemies/4/Cannonball1.png", "4 Enemies/5/Fly.png", "4 Enemies/6 (48x72)/Run.png",
            "6 Traps/1.png", "6 Traps/2.png", "6 Traps/3.png", "6 Traps/4.png", "6 Traps/5.png", "6 Traps/6.png",
            "1 Main Characters/Appearing.png", "5 GUI/Icons/Icon_01.png", "5 GUI/Interface/Tileset.png"]:
    print(*info(rel))

def sheet(items, name, scale, cols_w=900):
    # items: (label, relpath) disusun vertikal, tiap gambar diperbesar
    ims = [(l, Image.open(os.path.join(B, r)).convert("RGBA")) for l, r in items]
    W = max(i.width * scale for _, i in ims) + 10
    H = sum(i.height * scale + 16 for _, i in ims)
    canvas = Image.new("RGBA", (W, H), (70, 70, 90, 255))
    y = 0
    from PIL import ImageDraw
    d = ImageDraw.Draw(canvas)
    for l, i in ims:
        d.text((2, y), l, fill=(255, 255, 0, 255))
        y += 14
        canvas.alpha_composite(i.resize((i.width * scale, i.height * scale), Image.NEAREST), (0, y))
        y += i.height * scale + 2
    canvas.convert("RGB").save(os.path.join(OUT, name))

sheet([("tileset", "7 Levels/Tiled/Tileset.png")], "tileset.png", 4)
sheet([("hero1 idle", "1 Main Characters/1/Idle.png"), ("hero1 run", "1 Main Characters/1/Run.png"), ("hero2 idle", "1 Main Characters/2/Idle.png"),
       ("hero3 idle", "1 Main Characters/3/Idle.png"), ("hero1 hit", "1 Main Characters/1/Hit.png"), ("hero1 jump", "1 Main Characters/1/Jump.png"),
       ("hero1 fall", "1 Main Characters/1/Fall.png"), ("appearing", "1 Main Characters/Appearing.png")], "heroes.png", 3)
sheet([("e1 idle", "4 Enemies/1/Idle.png"), ("e1 run", "4 Enemies/1/Run.png"), ("e2 run", "4 Enemies/2/Run.png"), ("e3 walk", "4 Enemies/3/Walk.png"),
       ("e3 charge", "4 Enemies/3/Charge.png"), ("e4 walk", "4 Enemies/4/Walk.png"), ("e4 attack", "4 Enemies/4/Attack.png"), ("e5 fly", "4 Enemies/5/Fly.png"),
       ("e6 run", "4 Enemies/6 (48x72)/Run.png")], "enemies.png", 2)
sheet([("gem1", "3 Objects/Gems/1.png"), ("gem3", "3 Objects/Gems/3.png"), ("box1 idle", "3 Objects/Boxes/1_Idle.png"), ("box2 idle", "3 Objects/Boxes/2_Idle.png"),
       ("box1 hit", "3 Objects/Boxes/1_Hit.png"), ("box1 break", "3 Objects/Boxes/1_Break.png"), ("flag idle1", "3 Objects/Checkpoints/Checkpoint_Flag_Idle1.png"),
       ("flag out1", "3 Objects/Checkpoints/Checkpoint_Flag_Out1.png"), ("noflag", "3 Objects/Checkpoints/Checkpoint_No_Flag.png"),
       ("end idle", "3 Objects/Checkpoints/End_Idle.png"), ("end pressed", "3 Objects/Checkpoints/End_Pressed.png"), ("pointer idle", "3 Objects/Checkpoints/Pointer_Idle.png"),
       ("trap1", "6 Traps/1.png"), ("trap2", "6 Traps/2.png"), ("trap3", "6 Traps/3.png"), ("trap4", "6 Traps/4.png"), ("trap5", "6 Traps/5.png"), ("trap6", "6 Traps/6.png")],
      "objects.png", 3)
sheet([("bg%d" % i, "2 Locations/Backgrounds/%d.png" % i) for i in range(1, 7)] + [("gui tileset", "5 GUI/Interface/Tileset.png")], "bgs.png", 3)
print("ok")
