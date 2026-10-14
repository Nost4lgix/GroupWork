import random
    
card_types = [
    "panda", "dog", "squid", "cat", "chicken", 
    "cow", "rabbit", "bear", "fish", "turtle"
]

deck = card_types * 2  #card 20
card_states = ["hidden"] * 20
first_selection = None
second_selection = None
checking_timer = 0 

SPACING_X = 133
CARD_W = 100
CARD_H = 150

wrong_count = 0 #wrong count
start_time = None
#game_over = False
bg_img = None
plus_score = 0
delete_score = 0
score = 0
bonus = 0
stop = False
show_menu = True
menu_cards = []

def setup():
    global bg_img, menu_cards
    size(1500, 800)
    reset_game()
    bg_img = loadImage("game_bg.jpg")
    menu_cards = random.sample(card_types, 10)
    
def reset_game():                        
    global temp_time, pause_time, card_states,start_time, game_over, wrong_count, first_selection, second_selection, start_time, Real_time, delete_score, plus_score, bonus, score, win, stop
    card_states = ["hidden"] * 20
    first_selection = None
    second_selection = None
    random.shuffle(deck)
    wrong_count = 0
    start_time = None
    temp_time = 0
    pause_time = None
    countdown_time = 300
    Real_time = countdown_time
    game_over = False
    plus_score = 0
    delete_score = 0
    bonus = 0
    score = 0
    print("reset")
    win = False
    stop = False


def draw():
    global temp_time, checking_timer, first_selection, second_selection
    global wrong_count, countdown_time, Real_time, game_over
    global delete_score, plus_score, score, bonus, win, stop

    if show_menu:
        draw_start_screen()
        return

    background(180, 230, 255)

    # หน้าจอหยุดเกม
    if stop:
        fill(100, 100, 100, 220)
        rect(0, 0, width, height)

        fill(255)
        textAlign(CENTER, CENTER)
        textSize(40)
        text("GAME PAUSED", width/2, height/2 - 35)

        textSize(25)
        text("Click anywhere to continue", width/2, height/2 + 20)
        return

    countdown_time = 90  #1.3 minute *** 

    if start_time is None:
        Real_time = countdown_time
    else:
        if game_over == False and win == False:
            s_time = int((millis() - start_time) / 1000)
            Real_time = countdown_time - s_time + temp_time

        if not (card_states == ["matched"] * 20):
            stop_game(width, height)

    if (Real_time <= 0 and start_time is not None) or wrong_count > 25:
        game_over = True
        play_again(width, height)

    if card_states == ["matched"] * 20:
        win = True

    show_countdown(Real_time, width, height)

    if first_selection is not None and second_selection is not None:
        checking_timer += 1

        if checking_timer > 35:
            if deck[first_selection] == deck[second_selection]:
                card_states[first_selection] = "matched"
                card_states[second_selection] = "matched"
                plus_score += 1
                bonus += 1
            else:
                card_states[first_selection] = "hidden"
                card_states[second_selection] = "hidden"
                delete_score += 1
                bonus = 0
                wrong_count += 1

            if delete_score == 1:
                if Real_time >= 85:
                    score += 0
                elif Real_time >= 60:
                    score -= 1
                elif Real_time >= 40:
                    score -= 2
                elif Real_time >= 30:
                    score -= 3
                elif Real_time >= 10:
                    score -= 5

            if plus_score == 1:
                if Real_time >= 70:
                    score += 5
                elif Real_time >= 60:
                    score += 3
                elif Real_time >= 30:
                    score += 2
                elif Real_time >= 10:
                    score += 1

            if bonus >= 2:
                score += 10

            if score <= 0:
                score = 0

            plus_score = 0
            delete_score = 0
            first_selection = None
            second_selection = None
            checking_timer = 0

    for i in range(20):
        if i < 10:
            x = SPACING_X * (i + 1)
            y = height / 2.3
        else:
            x = SPACING_X * (i - 9)
            y = height / 1.5

        is_visible = (card_states[i] != "hidden")
        draw_card_by_type(deck[i], x, y, CARD_W, CARD_H, is_visible)

    if game_over:
        fill(255, 100, 100)
        textSize(40)
        textAlign(CENTER, BASELINE)
        text("YOU LOSE", width/2, height/3.5)

    if win:
        fill(255, 100, 100)
        textSize(40)
        textAlign(CENTER, BASELINE)
        text("You win", width/2, height/3.5)

    count_score(width, height)
    show_wrong(width, height)

        

def mousePressed():
    global first_selection, second_selection, card_states
    global start_time, stop, temp_time, pause_time, show_menu

    if show_menu:
        if (width/2-110 <= mouseX <= width/2+110 and
            390 <= mouseY <= 460):
            show_menu = False
            reset_game()
        elif (width/2-110 <= mouseX <= width/2+110 and
              490 <= mouseY <= 560):
            exit()
        return

    # ถ้ากำลังหยุดเกม ให้คลิกเพื่อเล่นต่อ
    if stop:
        stop = False
        temp_time += int((millis() - pause_time) / 1000)
        pause_time = None
        return

    # เลือกการ์ด
    for i in range(20):
        if i < 10:
            cx = SPACING_X * (i + 1)
            cy = height / 2.3
        else:
            cx = SPACING_X * (i - 9)
            cy = height / 1.5

        if (cx - CARD_W/2 <= mouseX <= cx + CARD_W/2 and
            cy - CARD_H/2 <= mouseY <= cy + CARD_H/2):

            if card_states[i] == "hidden":
                if first_selection is None:
                    first_selection = i
                    card_states[i] = "revealed"

                    if start_time is None:
                        start_time = millis()

                elif second_selection is None and i != first_selection:
                    second_selection = i
                    card_states[i] = "revealed"

            break

    # ปุ่ม Play again
    if (width/2.25 <= mouseX <= width/2.25 + width/10 and
        height/1.25 <= mouseY <= height/1.25 + height/10 and
        game_over):
        reset_game()
        return

    # ปุ่ม Stop
    if (width/1.17 <= mouseX <= width/1.17 + width/15 and
        height/5.25 <= mouseY <= height/5.25 + height/15 and
        start_time is not None):
        stop = True
        pause_time = millis()

    
def draw_card_by_type(card_type, x, y, w, h, is_visible):  
    if not is_visible:
        fill(180, 255, 180)
    else:
        fill(255)

    stroke(0)
    strokeWeight(1)
    rect(x - w/2, y - h/2, w, h, 10)
    
    if is_visible:
        if card_type == "panda":
            panda_card(x, y, w, is_visible)
        elif card_type == "dog":
            dog_card(x, y, w, is_visible)
        elif card_type == "squid":
            squid_card(x, y, w, is_visible)
        elif card_type == "cat":
            cat_card(x, y, w, is_visible)
        elif card_type == "chicken":
            chicken_card(x, y, w, is_visible)
        elif card_type == "cow":
            cow_card(x, y, w, is_visible)
        elif card_type == "rabbit":
            rabbit_card(x, y, w, is_visible)
        elif card_type == "bear":
            bear_card(x, y, w, is_visible)
        elif card_type == "fish":
            fish_card(x, y, w, is_visible)
        elif card_type == "turtle":
            turtle_card(x, y, w, is_visible)
            

def stop_game(w,h):
    fill(255)
    rect(w/1.17, h/5.25, w/15, h/15, 5)
    fill(0)
    textSize(40)
    textAlign(RIGHT, BASELINE)
    text("Stop",w/1.095, h/4.25)
    
def count_score(w,h):
    fill(0)
    textSize(40)
    textAlign(LEFT, BASELINE)
    text("score :",w/15,h/5)
    text(score,w/6.5,h/5)
    


def play_again(w,h):
    fill(255, 255, 220)
    rect(w/2.25, h/1.25, w/10, h/10, 10)
    fill(0)
    textSize(25)
    text("Play again",w/2.18,h/1.17)

            
def show_wrong(w,h):
    fill(0)
    textSize(40)
    textAlign(LEFT, BASELINE)
    text(wrong_count,w/6,h/7)
    text("/25",w/5,h/7)
    text("Wrong :",w/15,h/7)
    
def show_countdown(time,w,h):
    minutes = time // 60
    seconds = time % 60
    text_time = "{:02d}:{:02d}".format(minutes, seconds)
    textAlign(CENTER, BASELINE)
    fill(255, 100, 100)
    textSize(100)
    text(text_time,w/2,h/5)
    
#////////////////////////////////////////////////////////////////////////////////////////////////////

def dog(x,y,s):
    head_dog(x,y,s)
    eye2_dog(x,y,s)
    eye_dog(x,y,s)
    eye1_dog(x,y,s)
    nose_dog(x,y,s)
    mouth_dog(x,y,s)
    ear_dog(x,y,s)
    ear1_dog(x,y,s)
    cheek_dog(x,y,s)
    
def head_dog(x,y,s):
    fill(210,160,90)
    ellipse(x,y,s*2,s*2)

def ear_dog(x,y,s):
    fill(60,30,10)
    ellipse(x-(s/2),y-(s/1.5),s/1.7,s/1.8)

def ear1_dog(x,y,s):
    fill(210,150,80)
    ellipse(x+(s/2),y-(s/1.5),s/1.7,s/1.8)
    
def eye_dog(x,y,s):
    fill(20)
    ellipse(x-(s/3),y-(s/5),s/3,s/3)
    ellipse(x+(s/3),y-(s/5),s/3,s/3)
    
def eye1_dog(x,y,s):
    fill(255)
    ellipse(x-(s/2.5),y-(s/8),s/10,s/10)
    ellipse(x-(s/4),y-(s/4),s/8,s/8)
    ellipse(x+(s/4),y-(s/8),s/10,s/10)
    ellipse(x+(s/2.5),y-(s/4),s/8,s/8)
   
def eye2_dog(x,y,s):
    fill(255)
    ellipse(x+s/3,y-(s/5),s/2.5,s/2.5)
    
def nose_dog(x,y,s):
    fill(20)
    ellipse(x,y+(s/10),s/6,s/8)

def mouth_dog(x,y,s):
    line(x,y+(s/6),x,y+(s/3))
    line(x,y+(s/3),x-(s/8),y+(s/2.5))
    line(x,y+(s/3),x+(s/8),y+(s/2.5))
    
def cheek_dog(x,y,s):
    fill(245,253,208)
    ellipse(x-(s/2),y+(s/6),s/5,s/10)
    ellipse(x+(s/2),y+(s/6),s/5,s/10)
    
def dog_card(x,y,s,h):
    stroke(0)
    fill(255)
    if h:
        dog(x,y,s/4)
    return "dog"
    
def Panda(x,y,s):
    ear_Panda(x,y,s)
    ear1_Panda(x,y,s)
    head_Panda(x,y,s)
    eye_Panda(x,y,s)
    eye1_Panda(x,y,s)
    nose_Panda(x,y,s)
    mouth_Panda(x,y,s)
    
def ear_Panda(x,y,s):
    fill(100)
    ellipse(x-s/2,y-(s/1.5),s/1.5,s/1.5)
    ellipse(x+s/2,y-(s/1.5),s/1.5,s/1.5)
    
def ear1_Panda(x,y,s):
    fill(255,182,193)
    ellipse(x-s/2,y-(s/1.5),s/2,s/2)
    ellipse(x+s/2,y-(s/1.5),s/2,s/2)
    
def head_Panda(x,y,s):
    fill(255)
    ellipse(x,y,s*2,s*1.6)
    
def eye_Panda(x,y,s):
    fill(100)
    ellipse(x-(s/2.5),y-(s/5),s/2,s/2)
    ellipse(x+(s/2.5),y-(s/5),s/2,s/2)
    
def eye1_Panda(x,y,s):
    fill(255)
    ellipse(x-(s/2.8),y-(s/4),s/10,s/10)
    ellipse(x+(s/2.8),y-(s/4),s/10,s/10)
    
def nose_Panda(x,y,s):
    fill(100)
    ellipse(x,y+(s/20),s/8,s/10)
    
def mouth_Panda(x,y,s):
    fill(255,0,0)
    line(x,y+(s/10),x,y+(s/3))
    ellipse(x,y+(s/3),s/5,s/10)
    
def panda_card(x,y,s,h):
    stroke(0)
    fill(255)
    if h:
        Panda(x,y,s/4)
    return "Panda"

def squid(x,y,s):
    head_squid(x,y,s)
    eye_squid(x,y,s)
    nose_squid(x,y,s)
    nose1_squid(x,y,s)
    mouth_squid(x,y,s)
    
def head_squid(x,y,s):
    fill(255,182,200)
    ellipse(x,y,s*2,s*1.6)
    
def eye_squid(x,y,s):
    fill(0)
    ellipse(x-(s/2.5),y-(s/5),s/10,s/10)
    ellipse(x+(s/2.5),y-(s/5),s/10,s/10)
    
def nose_squid(x,y,s):
    fill(255,182,200)
    ellipse(x,y+(s/10),s/2,s/2)
    
def nose1_squid(x,y,s):
    fill(0)
    line(x-(s/10),y,x+(s/10),y+(s/5))
    line(x+(s/10),y,x-(s/10),y+(s/5))
    
def mouth_squid(x,y,s):
    fill(255,182,200)
    ellipse(x-(s/1.6),y+(s/1.3),s/3,s/2)
    ellipse(x-(s/3.4),y+(s/1.2),s/3,s/2)
    ellipse(x+(s/1.6),y+(s/1.3),s/3,s/2)
    ellipse(x+(s/2.8),y+(s/1.2),s/3,s/2)
    ellipse(x+(s/30),y+(s/1.2),s/3,s/2)
    
def squid_card(x,y,s,h):
    stroke(0)
    fill(255)
    if h:
        squid(x,y,s/4)
    return "squid"

def cat(x, y, s):
    ear_cat(x, y, s)        
    ear1_cat(x, y, s)    
    head_cat(x, y, s)      
    nuad_maew(x, y, s)        
    eye_cat(x, y, s)     
    eye1_cat(x, y, s)     
    nose_cat(x, y, s)     
    mouth_cat(x, y, s)    
    cheek_cat(x, y, s)     

def head_cat(x, y, s):
    fill(180) 
    ellipse(x, y, s*1.8, s*1.4)

def ear_cat(x, y, s): 
    fill(180)
    triangle(x-(s*0.75), y-(s*0.2),     
             x-(s*0.35), y-(s*0.65), 
             x-(s*0.75), y-(s*0.85))
    triangle(x+(s*0.75), y-(s*0.2),     
             x+(s*0.35), y-(s*0.65), 
             x+(s*0.75), y-(s*0.85))

def ear1_cat(x, y, s): 
    fill(255, 182, 193)
    triangle(x-(s*0.67), y-(s*0.28),    
             x-(s*0.38), y-(s*0.6), 
             x-(s*0.70), y-(s*0.78))
    triangle(x+(s*0.67), y-(s*0.28),    
             x+(s*0.38), y-(s*0.6), 
             x+(s*0.70), y-(s*0.78))

def nuad_maew(x, y, s):
    line(x-(s*0.4), y+(s*0.08), x-(s*0.85), y+(s*0.02))  
    line(x-(s*0.4), y+(s*0.16), x-(s*0.85), y+(s*0.16))
    line(x-(s*0.4), y+(s*0.24), x-(s*0.85), y+(s*0.30))
    
    line(x+(s*0.4), y+(s*0.08), x+(s*0.85), y+(s*0.02))  
    line(x+(s*0.4), y+(s*0.16), x+(s*0.85), y+(s*0.16))
    line(x+(s*0.4), y+(s*0.24), x+(s*0.85), y+(s*0.30))

def eye_cat(x, y, s): 
    fill(0)
    ellipse(x-(s*0.32), y-(s*0.08), s*0.25, s*0.28) 
    ellipse(x+(s*0.32), y-(s*0.08), s*0.25, s*0.28) 

def eye1_cat(x, y, s): 
    fill(255)
    ellipse(x-(s*0.36), y-(s*0.13), s*0.1, s*0.1)
    ellipse(x+(s*0.28), y-(s*0.13), s*0.1, s*0.1)

def nose_cat(x, y, s): 
    fill(255, 120, 150)
    ellipse(x, y+(s*0.06), s*0.12, s*0.08)

def mouth_cat(x, y, s): 
    line(x, y+(s/9), x , y+(s/4))
    line(x, y+(s/4), x-(s/9), y+(s/3))
    line(x, y+(s/4), x+(s/9), y+(s/3))

def cheek_cat(x, y, s): 
    noStroke()
    fill(255, 182, 193, 180)
    ellipse(x-(s*0.48), y+(s*0.1), s*0.2, s*0.12)
    ellipse(x+(s*0.48), y+(s*0.1), s*0.2, s*0.12)

def cat_card(x, y, s, h):
    stroke(0)
    fill(255) 
    if h:
        cat(x, y, s / 3)
    return "cat"

def chicken(x,y,s):
    ngon_kai(x,y,s)     
    head_chicken(x,y,s)    
    niang_kai(x,y,s)   
    pak_kai(x,y,s)         
    eye_kai(x,y,s)       
    eye1_kai(x,y,s)     
    cheek_kai(x,y,s)     

def ngon_kai(x,y,s): 
    fill(235,60,60)
    ellipse(x-(s*0.18), y-(s*0.65), s*0.22, s*0.32)
    ellipse(x, y-(s*0.72), s*0.26, s*0.38)
    ellipse(x+(s*0.18), y-(s*0.65), s*0.22, s*0.32)

def head_chicken(x,y,s):
    fill(255,245,180) 
    ellipse(x,y,s*1.6,s*1.4)

def niang_kai(x,y,s): 
    fill(235,60,60)
    ellipse(x-(s*0.07), y+(s*0.27), s*0.14, s*0.20)
    ellipse(x+(s*0.07), y+(s*0.27), s*0.14, s*0.20)

def pak_kai(x,y,s): 
    fill(255,140,0)
    triangle(x-(s*0.12), y+(s*0.06), 
             x+(s*0.12), y+(s*0.06), 
             x, y+(s*0.22))

def eye_kai(x,y,s): 
    stroke(0)
    fill(40)
    ellipse(x-(s*0.3), y-(s*0.08), s*0.23, s*0.26)
    ellipse(x+(s*0.3), y-(s*0.08), s*0.23, s*0.26)

def eye1_kai(x,y,s):
    fill(255)
    ellipse(x-(s*0.34), y-(s*0.13), s*0.09, s*0.09)
    ellipse(x+(s*0.26), y-(s*0.13), s*0.09, s*0.09)

def cheek_kai(x,y,s): 
    noStroke()
    fill(255, 182, 193, 180)
    ellipse(x-(s*0.48), y+(s*0.1), s*0.2, s*0.12)
    ellipse(x+(s*0.48), y+(s*0.1), s*0.2, s*0.12)

def chicken_card(x,y,s,h):
    stroke(0)
    fill(255) 
    if h:
        chicken(x, y, s/3)
    return "chicken"

def cow(x, y, s):
    khao_wua(x, y, s)    
    ear_cow(x, y, s)
    ear1_cow(x, y, s)      
    head_cow(x, y, s)      
    spot_cow(x, y, s)     
    snout_cow(x, y, s)    
    nose_cow(x, y, s)      
    eye2_cow(x, y, s)     
    eye_cow(x, y, s)       
    eye1_cow(x, y, s)      
    cheek_cow(x, y, s)    

def khao_wua(x, y, s): 
    fill(240, 200, 120)
    ellipse(x - (s * 0.38), y - (s * 0.52), s * 0.24, s * 0.38)
    ellipse(x + (s * 0.38), y - (s * 0.52), s * 0.2, s * 0.38)

def ear_cow(x, y, s): 
    stroke(0)
    fill(255)
    ellipse(x - (s * 0.65), y - (s * 0.22), s * 0.45, s * 0.25)
    ellipse(x + (s * 0.65), y - (s * 0.22), s * 0.45, s * 0.25)

def ear1_cow(x, y, s): 
    stroke(0)
    fill(255, 182, 193)
    ellipse(x - (s * 0.65), y - (s * 0.22), s * 0.28, s * 0.15)
    ellipse(x + (s * 0.65), y - (s * 0.22), s * 0.28, s * 0.15)

def head_cow(x, y, s): 
    stroke(0)
    fill(255)
    ellipse(x, y, s * 1.6, s * 1.4)

def spot_cow(x, y, s): 
    noStroke()
    fill(40)
    ellipse(x - (s * 0.38), y - (s * 0.2), s * 0.45, s * 0.45)

def snout_cow(x, y, s): 
    stroke(0)
    fill(255, 190, 200)
    ellipse(x, y + (s * 0.18), s * 0.75, s * 0.42)

def nose_cow(x, y, s): 
    stroke(0)
    fill(40)
    ellipse(x - (s * 0.12), y + (s * 0.14), s * 0.08, s * 0.12)
    ellipse(x + (s * 0.12), y + (s * 0.14), s * 0.08, s * 0.12)

def eye2_cow(x, y, s): 
    stroke(0)
    fill(255)
    ellipse(x - (s * 0.3), y - (s * 0.08), s * 0.3, s * 0.33)
    ellipse(x + (s * 0.3), y - (s * 0.08), s * 0.3, s * 0.33)

def eye_cow(x, y, s): 
    stroke(0)
    fill(40)
    ellipse(x - (s * 0.3), y - (s * 0.08), s * 0.23, s * 0.26)
    ellipse(x + (s * 0.3), y - (s * 0.08), s * 0.23, s * 0.26)

def eye1_cow(x, y, s): 
    noStroke()
    fill(255)
    ellipse(x - (s * 0.34), y - (s * 0.13), s * 0.09, s * 0.09)
    ellipse(x + (s * 0.26), y - (s * 0.13), s * 0.09, s * 0.09)

def cheek_cow(x, y, s): 
    noStroke()
    fill(255, 182, 193, 180)
    ellipse(x - (s * 0.48), y + (s * 0.05), s * 0.2, s * 0.12)
    ellipse(x + (s * 0.48), y + (s * 0.05), s * 0.2, s * 0.12)

def cow_card(x, y, s, h):
    stroke(0)
    fill(255) 
    if h:
        cow(x, y, s / 3)
    return "cow"

def rabbit(x,y,s):
    ear_rabbit(x,y,s)
    ear1_rabbit(x,y,s)
    head_rabbit(x,y,s)
    eye_rabbit(x,y,s)
    eye1_rabbit(x,y,s)
    nose_rabbit(x,y,s)
    mouth_rabbit(x,y,s)
    cheek_rabbit(x,y,s)

def head_rabbit(x,y,s):
    fill(255)
    ellipse(x, y, s*1.8, s*1.5)

def ear_rabbit(x, y, s): 
    fill(255)
    ellipse(x-(s/3), y-(s/1.1), s/2.5,s*1.3)
    ellipse(x+(s/3), y-(s/1.1), s/2.5,s*1.3)

def ear1_rabbit(x, y, s): 
    fill(255, 182, 193)
    ellipse(x-(s/3), y-(s/1.1), s/5,s)
    ellipse(x+(s/3), y-(s/1.1), s/5,s)

def eye_rabbit(x, y, s): 
    fill(40)
    ellipse(x-(s/3), y-(s/6), s/4,s/4)
    ellipse(x+(s/3), y-(s/6), s/4,s/4)

def eye1_rabbit(x, y, s): 
    fill(255)
    ellipse(x-(s/2.8), y-(s/4), s/10, s/10)
    ellipse(x+(s/3.3), y-(s/4), s/10, s/10)

def nose_rabbit(x, y, s):
    fill(255, 120, 150)
    ellipse(x, y+(s/10), s/8, s/12) 

def mouth_rabbit(x, y, s):
    noFill()
    line(x, y+(s/7), x , y+(s/4))
    line(x, y+(s/4), x-(s/10), y+(s/3))
    line(x, y+(s/4), x+(s/10), y+(s/3))

def cheek_rabbit(x, y, s):
    fill(255, 182, 193)
    ellipse(x-(s/2), y+(s/8), s/4, s/6)
    ellipse(x+(s/2), y+(s/8), s/4, s/6)

def rabbit_card(x, y, s, h):
    stroke(0)
    fill(255) 
    if h:
        rabbit(x, y, s / 3)
    return "rabbit"

def bear(x, y, s):
    bear_ears(x, y, s)
    bear_head(x, y, s)
    bear_muzzle(x, y, s)
    bear_nose(x, y, s)
    bear_eyes(x, y, s)

def bear_ears(x, y, s):
    fill(130, 85, 50)
    ellipse(x - s * 0.7, y - s * 0.7, s * 0.6, s * 0.6)
    ellipse(x + s * 0.7, y - s * 0.7, s * 0.6, s * 0.6)
    
    fill(185, 135, 95)
    ellipse(x - s * 0.7, y - s * 0.7, s * 0.35, s * 0.35)
    ellipse(x + s * 0.7, y - s * 0.7, s * 0.35, s * 0.35)

def bear_head(x, y, s):
    fill(150, 100, 60)
    ellipse(x, y, s * 1.8, s * 1.6)

def bear_muzzle(x, y, s):
    fill(215, 175, 135)
    ellipse(x, y + s * 0.25, s * 0.8, s * 0.6)

def bear_nose(x, y, s):
    fill(35, 25, 20)
    ellipse(x, y + s * 0.12, s * 0.3, s * 0.2)
    line(x, y + s * 0.22, x, y + s * 0.38)
    line(x, y + s * 0.38, x - s * 0.15, y + s * 0.45)
    line(x, y + s * 0.38, x + s * 0.15, y + s * 0.45)

def bear_eyes(x, y, s):
    fill(25)
    ellipse(x - s * 0.4, y - s * 0.1, s * 0.18, s * 0.18)
    ellipse(x + s * 0.4, y - s * 0.1, s * 0.18, s * 0.18)
    fill(255)
    ellipse(x - s * 0.42, y - s * 0.12, s * 0.06, s * 0.06)
    ellipse(x + s * 0.38, y - s * 0.12, s * 0.06, s * 0.06)

def bear_card(x, y, s, h):
    fill(255)
    if h:
        bear(x, y, s / 3)
    return "bear"

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
    if h:
        fish(x, y, s / 3)
    return "fish"

def turtle(x, y, s):
    turtle_feet(x, y, s)
    turtle_tail(x, y, s)
    turtle_shell(x, y, s)
    turtle_head(x, y, s)
    turtle_eyes(x, y, s)

def turtle_feet(x, y, s):
    fill(95, 145, 80)
    ellipse(x - s * 0.7, y - s * 0.5, s * 0.5, s * 0.35)
    ellipse(x + s * 0.7, y - s * 0.5, s * 0.5, s * 0.35)
    ellipse(x - s * 0.6, y + s * 0.5, s * 0.45, s * 0.35)
    ellipse(x + s * 0.6, y + s * 0.5, s * 0.45, s * 0.35)

def turtle_tail(x, y, s):
    fill(95, 145, 80)
    triangle(x - s * 0.15, y + s * 0.8, x + s * 0.15, y + s * 0.8, x, y + s * 1.1)

def turtle_shell(x, y, s):
    fill(60, 110, 50)
    ellipse(x, y, s * 1.6, s * 1.8)

def turtle_head(x, y, s):
    fill(110, 165, 95)
    ellipse(x, y - s * 0.85, s * 0.6, s * 0.7)

def turtle_eyes(x, y, s):
    fill(255)
    ellipse(x - s * 0.18, y - s * 0.95, s * 0.18, s * 0.18)
    ellipse(x + s * 0.18, y - s * 0.95, s * 0.18, s * 0.18)
    fill(20)
    ellipse(x - s * 0.18, y - s * 0.95, s * 0.08, s * 0.08)
    ellipse(x + s * 0.18, y - s * 0.95, s * 0.08, s * 0.08)

def turtle_card(x, y, s, h):
    fill(255)
    if h:
        turtle(x, y, s / 3)
    return "turtle"

def draw_start_screen():
    background(255)

    # Three randomly selected animal cards, tilted for decoration
    positions = [
        # ด้านซ้าย
        (100, 160, -0.20),
        (220, 330, 0.15),
        (100, 500, -0.15),
        (300, 650, 0.20),

        # ด้านขวา
        (1200, 160, 0.20),
        (1380, 300, -0.15),
        (1200, 500, 0.15),
        (1380, 650, -0.20),

        # ด้านบน
        (500, 100, -0.15),
        (1000, 100, 0.15)
    ]

    for i in range(10):
        x, y, angle = positions[i]
        pushMatrix()
        translate(x, y)
        rotate(angle)
        draw_card_by_type(menu_cards[i], 0, 0, CARD_W, CARD_H, True)
        popMatrix()

    # Game title
    fill(70, 70, 80)
    textAlign(CENTER, CENTER)
    textSize(64)
    text("Matching Card Game", width/2, 220)

    fill(170, 170, 180)
    textSize(24)
    text("Find the matching animals!", width/2, 285)

    # PLAY button
    noStroke()
    fill(255, 190, 205)
    rect(width/2-110, 390, 220, 70, 20)
    fill(70, 70, 80)
    textSize(30)
    text("PLAY", width/2, 425)
