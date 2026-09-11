hidden = True

def setup():
    size(800, 800)

def turtle(x, y, s):
    turtle_feet(x, y, s)
    turtle_tail(x, y, s)
    turtle_shell(x, y, s)
    turtle_head(x, y, s)
    turtle_eyes(x, y, s)

def turtle_feet(x, y, s):
    fill(95, 145, 80)
    # ขาหน้า 2 ข้าง
    ellipse(x - s * 0.7, y - s * 0.5, s * 0.5, s * 0.35)
    ellipse(x + s * 0.7, y - s * 0.5, s * 0.5, s * 0.35)
    # ขาหลัง 2 ข้าง
    ellipse(x - s * 0.6, y + s * 0.5, s * 0.45, s * 0.35)
    ellipse(x + s * 0.6, y + s * 0.5, s * 0.45, s * 0.35)

def turtle_tail(x, y, s):
    fill(95, 145, 80)
    triangle(x - s * 0.15, y + s * 0.8, x + s * 0.15, y + s * 0.8, x, y + s * 1.1)

def turtle_shell(x, y, s):
    # กระดองหลัก
    fill(60, 110, 50)
    ellipse(x, y, s * 1.6, s * 1.8)

def turtle_head(x, y, s):
    fill(110, 165, 95)
    ellipse(x, y - s * 0.85, s * 0.6, s * 0.7)

def turtle_eyes(x, y, s):
    # ตาขาว
    fill(255)
    ellipse(x - s * 0.18, y - s * 0.95, s * 0.18, s * 0.18)
    ellipse(x + s * 0.18, y - s * 0.95, s * 0.18, s * 0.18)
    # ตาดำจุดเล็กๆ
    fill(20)
    ellipse(x - s * 0.18, y - s * 0.95, s * 0.08, s * 0.08)
    ellipse(x + s * 0.18, y - s * 0.95, s * 0.08, s * 0.08)

def turtle_card(x, y, s, h):
    fill(255)
    rect(x - (s / 2), y - (s * 1.5) / 2, s, s * 1.5)
    if h:
        turtle(x, y, s / 3)
    return "turtle"

def draw():
    background(255)
    turtle_card(width / 2, height / 2, 200, hidden)
