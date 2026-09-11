hidden = True

def setup():
    size(800, 800)

def fish(x, y, s):
    cx = x + s * 0.22
    cy = y + s * 0.05
    
    fish_tail_fin(cx, cy, s)
    fish_dorsal_fin(cx, cy, s)
    fish_body(cx, cy, s)
    fish_eye(cx, cy, s)


def fish_tail_fin(x, y, s):
    fill(235, 100, 70)
    triangle(x - s * 0.7, y, x - s * 1.3, y - s * 0.6, x - s * 1.3, y + s * 0.6)

def fish_dorsal_fin(x, y, s):
    fill(235, 100, 70)
    triangle(x - s * 0.3, y - s * 0.45, x + s * 0.1, y - s * 0.45, x - s * 0.1, y - s * 0.9)

def fish_body(x, y, s):
    fill(250, 130, 85)
    ellipse(x, y, s * 1.7, s * 1.0)

def fish_eye(x, y, s):
    fill(255)
    ellipse(x + s * 0.45, y - s * 0.15, s * 0.28, s * 0.28)
    fill(20)
    ellipse(x + s * 0.48, y - s * 0.15, s * 0.14, s * 0.14)
    fill(255)
    ellipse(x + s * 0.50, y - s * 0.18, s * 0.05, s * 0.05)



def fish_card(x, y, s, h):
    fill(255)
    rect(x - (s / 2), y - (s * 1.5) / 2, s, s * 1.5)
    if h:
        fish(x, y, s / 3)
    return "fish"

def draw():
    background(255)
    fish_card(width / 2, height / 2, 200, hidden)
