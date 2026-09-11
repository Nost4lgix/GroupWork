hidden = True

def setup():
    size(800, 800)

def bear(x, y, s):
    bear_ears(x, y, s)
    bear_head(x, y, s)
    bear_muzzle(x, y, s)
    bear_nose(x, y, s)
    bear_eyes(x, y, s)

def bear_ears(x, y, s):
    # หูด้านนอก (สีน้ำตาลเข้ม)
    fill(130, 85, 50)
    ellipse(x - s * 0.7, y - s * 0.7, s * 0.6, s * 0.6)
    ellipse(x + s * 0.7, y - s * 0.7, s * 0.6, s * 0.6)
    
    # หูด้านใน (สีน้ำตาลอ่อน)
    fill(185, 135, 95)
    ellipse(x - s * 0.7, y - s * 0.7, s * 0.35, s * 0.35)
    ellipse(x + s * 0.7, y - s * 0.7, s * 0.35, s * 0.35)

def bear_head(x, y, s):
    # หัวหมี
    fill(150, 100, 60)
    ellipse(x, y, s * 1.8, s * 1.6)

def bear_muzzle(x, y, s):
    # วงรีตรงบริเวณปาก/จมูก
    fill(215, 175, 135)
    ellipse(x, y + s * 0.25, s * 0.8, s * 0.6)

def bear_nose(x, y, s):
    # จมูก
    fill(35, 25, 20)
    ellipse(x, y + s * 0.12, s * 0.3, s * 0.2)
    # ปาก
    line(x, y + s * 0.22, x, y + s * 0.38)
    line(x, y + s * 0.38, x - s * 0.15, y + s * 0.45)
    line(x, y + s * 0.38, x + s * 0.15, y + s * 0.45)

def bear_eyes(x, y, s):
    # ตา
    fill(25)
    ellipse(x - s * 0.4, y - s * 0.1, s * 0.18, s * 0.18)
    ellipse(x + s * 0.4, y - s * 0.1, s * 0.18, s * 0.18)
    # ไฮไลต์ตา
    fill(255)
    ellipse(x - s * 0.42, y - s * 0.12, s * 0.06, s * 0.06)
    ellipse(x + s * 0.38, y - s * 0.12, s * 0.06, s * 0.06)

def bear_card(x, y, s, h):
    fill(255)
    rect(x - (s / 2), y - (s * 1.5) / 2, s, s * 1.5)
    if h:
        bear(x, y, s / 3)
    return "bear"

def draw():
    background(255)
    bear_card(width / 2, height / 2, 200, hidden)
