#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain = Brain()

# Define motors on Port 1 and Port 5 (Motor 5 reversed to align chassis direction)
motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_5 = Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)

# Set active braking mode to prevent momentum coasting
motor_1.set_stopping(HOLD)
motor_5.set_stopping(HOLD)

# Wait for motors to fully initialize
wait(100, MSEC)

# Generating and setting random seed
def initializeRandomSeed():
    wait(100, MSEC)
    systemTime = brain.timer.system() * 100
    urandom.seed(int(systemTime)) 

# Initialize random seed 
initializeRandomSeed()
#endregion VEXcode Generated Robot Configuration

# -------------------------------------------------------------
# FULL-SCREEN CARD GRAPHIC DISPLAY FUNCTION
# -------------------------------------------------------------

def draw_card_full_screen(card_str, color_code):
    brain.screen.clear_screen()
    if color_code == 'R': brain.screen.set_fill_color(Color.RED)
    elif color_code == 'G': brain.screen.set_fill_color(Color.GREEN)
    elif color_code == 'B': brain.screen.set_fill_color(Color.BLUE)
    elif color_code == 'Y': brain.screen.set_fill_color(Color.YELLOW)
    else: brain.screen.set_fill_color(Color.BLACK)
    brain.screen.set_pen_color(Color.WHITE)
    for i in range(5):
        brain.screen.draw_rectangle(0+i, 0+i, 159-(i*2), 107-(i*2))
   
    card = card_str[1:] if len(card_str) > 1 else card_str
    if card == "0":
        for i in range(15):
            brain.screen.draw_rectangle(20+i, 20+i, 119-(i*2), 67-(i*2))
    elif card == "8":
        for i in range(15):
            brain.screen.draw_rectangle(20+i, 20+i, 119-(i*2), 67-(i*2))
        for i in range(15):
            brain.screen.draw_line(72+i, 20, 72+i, 85)
    elif card == "1":
        for i in range(15):
            brain.screen.draw_line(20, 47+i, 139, 47+i)
    elif card == "3":
        for i in range(15):
            brain.screen.draw_line(20, 20+i, 139, 20+i)
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
    elif card == "2":
        for i in range(15):
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(20, 20+i, 72, 20+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 73+i, 139, 73+i)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
        for i in range(3):
            brain.screen.draw_line(145+i, 20, 145+i, 87)
    elif card == "5":
        for i in range(15):
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(20, 73+i, 72, 73+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 20+i, 139, 20+i)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
        for i in range(3):
            brain.screen.draw_line(145+i, 20, 145+i, 87)
    elif card == "6":
        for i in range(15):
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(20, 73+i, 72, 73+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 20+i, 139, 20+i)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
            brain.screen.draw_line(72, 73+i, 139, 73+i)
        for i in range(3):
            brain.screen.draw_line(145+i, 20, 145+i, 87)
    elif card == "9":
        for i in range(15):
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(20, 20+i, 72, 20+i)
            brain.screen.draw_line(20, 73+i, 72, 73+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 20+i, 139, 20+i)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
        for i in range(3):
            brain.screen.draw_line(145+i, 20, 145+i, 87)
    elif card == "4" and "D" not in card_str:
        for i in range(15):
            brain.screen.draw_line(20, 20+i, 72, 20+i)
            brain.screen.draw_line(20, 73+i, 72, 73+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 20+i, 139, 20+i)
    elif card == "7":
        for i in range(15):
            brain.screen.draw_line(20, 20+i, 139, 20+i)
            brain.screen.draw_line(20+i, 20, 20+i, 87)
    elif card == "Rv":
        for i in range(15):
            brain.screen.draw_line(62+i, 30, 62+i, 87)
            brain.screen.draw_line(69, 20, 52+i, 40)
            brain.screen.draw_line(69, 20, 82-i, 40)
            brain.screen.draw_line(82+i, 20, 82+i, 77)
            brain.screen.draw_line(89, 87, 74+i, 67)
            brain.screen.draw_line(89, 87, 104-i, 67)
    elif card == "S":
        for i in range(15):
            brain.screen.draw_rectangle(40+i, 20+i, 82-(i*2), 67-(i*2))
        for i in range(15):
            brain.screen.draw_line(52+i, 20, 92+i, 80)
    elif card == "D2":
        brain.screen.set_fill_color(Color.WHITE)
        for i in range(40):
            brain.screen.draw_circle(60+i, 42+(i/2), 30)
        if color_code == 'R': brain.screen.set_fill_color(Color.RED)
        elif color_code == 'G': brain.screen.set_fill_color(Color.GREEN)
        elif color_code == 'B': brain.screen.set_fill_color(Color.BLUE)
        elif color_code == 'Y': brain.screen.set_fill_color(Color.YELLOW)
        brain.screen.draw_rectangle(47, 32, 40, 25)
        brain.screen.draw_rectangle(73, 52, 40, 25)
        for i in range(5):
            brain.screen.draw_line(18+i, 85, 18+i, 95)
            brain.screen.draw_line(14, 88+i, 26, 88+i)
            brain.screen.draw_line(10+i, 66, 10+i, 79)
            brain.screen.draw_line(10, 66+i, 20, 66+i)
            brain.screen.draw_line(18+i, 66, 18+i, 79)
            brain.screen.draw_line(20, 75+i, 30, 75+i)
            brain.screen.draw_line(26+i, 66, 26+i, 79)

            brain.screen.draw_line(159-18-i, 107-85, 159-18-i, 107-95)
            brain.screen.draw_line(159-14, 107-88-i, 159-26, 107-88-i)
            brain.screen.draw_line(159-10-i, 107-66, 159-10-i, 107-79)
            brain.screen.draw_line(159-10, 107-66-i, 159-20, 107-66-i)
            brain.screen.draw_line(159-18-i, 107-66, 159-18-i, 107-79)
            brain.screen.draw_line(159-20, 107-75-i, 159-30, 107-75-i)
            brain.screen.draw_line(159-26-i, 107-66, 159-26-i, 107-79)
    elif card_str == "W":
        brain.screen.set_fill_color(Color.BLUE)
        brain.screen.draw_rectangle(50, 20, 30, 32)
        brain.screen.set_fill_color(Color.RED)
        brain.screen.draw_rectangle(50, 52, 30, 32)
        brain.screen.set_fill_color(Color.GREEN)
        brain.screen.draw_rectangle(80, 20, 30, 32)
        brain.screen.set_fill_color(Color.YELLOW)
        brain.screen.draw_rectangle(80, 52, 30, 32)
        brain.screen.set_fill_color(Color.TRANSPARENT)
        brain.screen.set_pen_width(3)
        for i in range(15):
            brain.screen.draw_circle(80, 52, 30-(i/5))
        brain.screen.set_pen_color(Color.BLACK)
        for i in range(65):
            brain.screen.draw_circle(80, 52, 31+(i/5))
        brain.screen.set_pen_width(1)
    elif card_str == "D4":
        brain.screen.set_fill_color(Color.YELLOW)
        brain.screen.draw_rectangle(78, 42, 40, 25)
        brain.screen.set_fill_color(Color.GREEN)
        brain.screen.draw_rectangle(60, 28, 40, 25)
        brain.screen.set_fill_color(Color.BLUE)
        brain.screen.draw_rectangle(42, 42, 40, 25)
        brain.screen.set_fill_color(Color.RED)
        brain.screen.draw_rectangle(60, 56, 40, 25)
        for i in range(5):
            brain.screen.draw_line(18+i, 85, 18+i, 95)
            brain.screen.draw_line(14, 88+i, 26, 88+i)
            brain.screen.draw_line(10, 75+i, 20, 75+i)
            brain.screen.draw_line(16+i, 75, 16+i, 66)
            brain.screen.draw_line(10, 66+i, 30, 66+i)

            brain.screen.draw_line(159-18-i, 107-85, 159-18-i, 107-95)
            brain.screen.draw_line(159-14, 107-88-i, 159-26, 107-88-i)
            brain.screen.draw_line(159-10, 107-75-i, 159-20, 107-75-i)
            brain.screen.draw_line(159-16-i, 107-75, 159-16-i, 107-66)
            brain.screen.draw_line(159-10, 107-66-i, 159-30, 107-66-i)
    else:
        # Default UNO Card Back Graphic
        brain.screen.set_fill_color(Color.RED)
        brain.screen.set_pen_color(Color.RED)
        for i in range(40):
            brain.screen.draw_circle(60+i, 42+(i/2), 30)
        brain.screen.set_pen_color(Color.YELLOW)
        for i in range(5):
            brain.screen.draw_line(75, 50+i-5, 85, 50+i-5)
            brain.screen.draw_line(75, 50+i+5, 85, 50+i+5)
            brain.screen.draw_line(75, 50+i+5, 85, 50+i-5)

            brain.screen.draw_line(75, 50+i-15, 85, 50+i-15)
            brain.screen.draw_line(75+(i/2), 50-15, 75+(i/2), 50-25)
            brain.screen.draw_line(83+(i/2), 50-15, 83+(i/2), 50-25)
            brain.screen.draw_line(75, 50+i-25, 85, 50+i-25)

            brain.screen.draw_line(75, 50+i+15, 85, 50+i+15)
            brain.screen.draw_line(83+(i/2), 50+15, 83+(i/2), 50+25)
            brain.screen.draw_line(75, 50+i+25, 85, 50+i+25)
    brain.screen.set_fill_color(Color.TRANSPARENT)

def display_card_graphic(card_name):
    if card_name is None:
        draw_card_full_screen("BACK", "")
        return

    parts = card_name.split(" ")
    c_color = parts[0]
    color_code = ''
    if c_color == "Red": color_code = 'R'
    elif c_color == "Green": color_code = 'G'
    elif c_color == "Blue": color_code = 'B'
    elif c_color == "Yellow": color_code = 'Y'

    val = " ".join(parts[1:])
    if val == "Wild":
        card_str = "W"
        color_code = ''
    elif val == "Wild Draw 4":
        card_str = "D4"
        color_code = ''
    elif val == "Draw 2":
        card_str = color_code + "D2"
    elif val == "Skip":
        card_str = color_code + "S"
    elif val == "Reverse":
        card_str = color_code + "Rv"
    else:
        card_str = color_code + val

    draw_card_full_screen(card_str, color_code)

# Flashes exactly 1 card back per drawn card
def flash_card_back_once():
    draw_card_full_screen("BACK", "")
    wait(350, MSEC)
    brain.screen.clear_screen()
    wait(150, MSEC)

# -------------------------------------------------------------
# HARDWARE ENCODER MOVEMENT ROUTINE
# -------------------------------------------------------------

def drive_straight_encoder(target_degrees, base_speed=35):
    motor_1.reset_position()
    motor_5.reset_position()
    motor_1.set_stopping(HOLD)
    motor_5.set_stopping(HOLD)
    
    kp = 0.4
    
    motor_1.spin(FORWARD)
    motor_5.spin(FORWARD)
    
    while abs(motor_1.position(DEGREES)) < target_degrees:
        left_pos = abs(motor_1.position(DEGREES))
        right_pos = abs(motor_5.position(DEGREES))
        
        error = left_pos - right_pos
        
        left_speed = base_speed - (error * kp)
        right_speed = base_speed + (error * kp)
        
        left_speed = max(5, min(100, left_speed))
        right_speed = max(5, min(100, right_speed))
        
        motor_1.set_velocity(left_speed, PERCENT)
        motor_5.set_velocity(right_speed, PERCENT)
        
        wait(10, MSEC)
        
    motor_1.stop(HOLD)
    motor_5.stop(HOLD)

def motor1_turn_left():
    motor_1.spin_for(REVERSE, 220, DEGREES, False)

def motor5_turn_left():
    motor_5.spin_for(FORWARD, 220, DEGREES, True)

def drive_to_center():
    draw_card_full_screen("BACK", "")
    drive_straight_encoder(850, base_speed=35)
    wait(150, MSEC)

def drive_back_to_player():
    # Hide face-up card display while driving back (show card back)
    draw_card_full_screen("BACK", "")
    
    # Turn 180 degrees toward home
    motor1_turn_left()
    motor5_turn_left()
    wait(150, MSEC)
    motor1_turn_left()
    motor5_turn_left()
    wait(150, MSEC)
    
    # Drive back toward home station
    drive_straight_encoder(850, base_speed=35)
    wait(150, MSEC)
    
    # Turn 180 degrees back to face center
    motor1_turn_left()
    motor5_turn_left()
    wait(150, MSEC)
    motor1_turn_left()
    motor5_turn_left()
    wait(150, MSEC)

# -------------------------------------------------------------
# UNO GAME TRACKER & DECK MANAGER
# -------------------------------------------------------------

def create_shuffled_uno_deck():
    colors = ['Red', 'Yellow', 'Green', 'Blue']
    actions = ['Skip', 'Reverse', 'Draw 2']
    deck = []

    for color in colors:
        deck.append(color + " 0")
        for number in range(1, 10):
            deck.append(color + " " + str(number))
            deck.append(color + " " + str(number))
        for action in actions:
            deck.append(color + " " + action)
            deck.append(color + " " + action)
        deck.append(color + " Wild")
        deck.append(color + " Wild Draw 4")

    for i in range(len(deck) - 1, 0, -1):
        j = urandom.randint(0, i)
        deck[i], deck[j] = deck[j], deck[i]

    return deck

def draw_card(deck):
    if len(deck) > 0:
        return deck.pop(0)
    return None

def start_game(deck):
    hand = []
    for _ in range(7):
        card = draw_card(deck)
        if card != None:
            hand.append(card)
    return hand

def print_hand_to_console(hand):
    print("=== YOUR HAND (" + str(len(hand)) + " CARDS) ===")
    for index, card in enumerate(hand, 1):
        print("Card " + str(index) + ": " + card)

def shorten_card(card):
    parts = card.split(" ")
    color = parts[0][0]  # 'R', 'Y', 'G', 'B'
    val = " ".join(parts[1:])
    
    if val == "Wild Draw 4":
        return color + "+4"
    if val == "Draw 2":
        return color + "+2"
    if val == "Skip":
        return color + "Sk"
    if val == "Reverse":
        return color + "Rv"
    if val == "Wild":
        return color + "W"
    
    return color + val

def wait_for_button_click():
    while True:
        if brain.buttonLeft.pressing():
            while brain.buttonLeft.pressing():
                wait(20, MSEC)
            return "LEFT"
        elif brain.buttonRight.pressing():
            while brain.buttonRight.pressing():
                wait(20, MSEC)
            return "RIGHT"
        elif brain.buttonCheck.pressing():
            while brain.buttonCheck.pressing():
                wait(20, MSEC)
            return "CHECK"
        wait(20, MSEC)

def choose_wild_color(wild_type):
    colors = ["Red", "Yellow", "Green", "Blue"]
    idx = 0
    
    while True:
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.print("CHOOSE WILD COLOR")
        brain.screen.set_cursor(2, 1)
        brain.screen.print("< " + colors[idx] + " >")
        brain.screen.set_cursor(4, 1)
        brain.screen.print("L/R:Nav CHK:Pick")
        
        btn = wait_for_button_click()
        if btn == "LEFT":
            idx = (idx - 1) % len(colors)
        elif btn == "RIGHT":
            idx = (idx + 1) % len(colors)
        elif btn == "CHECK":
            selected_color = colors[idx]
            break

    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("COLOR CHOSEN:")
    brain.screen.set_cursor(2, 1)
    brain.screen.print("--> " + selected_color + " <--")
    brain.screen.set_cursor(5, 1)
    brain.screen.print("CHK: Continue")
    wait_for_button_click()

    return selected_color + " " + wild_type

def print_hand_to_screen(hand, status_msg=""):
    page = 0
    cards_per_page = 9
    
    while True:
        brain.screen.clear_screen()
        total_cards = len(hand)
        total_pages = (total_cards + cards_per_page - 1) // cards_per_page
        if total_pages == 0:
            total_pages = 1
            
        if total_pages > 1:
            header = "HAND(" + str(total_cards) + ") P" + str(page + 1) + "/" + str(total_pages)
        else:
            header = "HAND (" + str(total_cards) + " cards)"
            
        brain.screen.set_cursor(1, 1)
        brain.screen.print(header[0:16])
        
        start_idx = page * cards_per_page
        end_idx = min(start_idx + cards_per_page, total_cards)
        page_cards = []
        for index in range(start_idx, end_idx):
            page_cards.append(str(index + 1) + ":" + shorten_card(hand[index]))
            
        line1 = ""
        line2 = ""
        line3 = ""
        
        for i in range(len(page_cards)):
            if i < 3:
                line1 = line1 + page_cards[i] + " "
            elif i < 6:
                line2 = line2 + page_cards[i] + " "
            elif i < 9:
                line3 = line3 + page_cards[i] + " "
                
        brain.screen.set_cursor(2, 1)
        brain.screen.print(line1[0:16])
        brain.screen.set_cursor(3, 1)
        brain.screen.print(line2[0:16])
        brain.screen.set_cursor(4, 1)
        brain.screen.print(line3[0:16])
        
        brain.screen.set_cursor(5, 1)
        if total_pages > 1:
            brain.screen.print("L/R:Pg CHK:Done")
        else:
            if status_msg != "":
                brain.screen.print(status_msg[0:16])
            else:
                brain.screen.print("CHK: Continue")
                
        btn = wait_for_button_click()
        if btn == "LEFT" and total_pages > 1:
            page = (page - 1) % total_pages
        elif btn == "RIGHT" and total_pages > 1:
            page = (page + 1) % total_pages
        elif btn == "CHECK":
            break

def check_attack_status():
    options = ["NONE", "DRAW +2", "DRAW +4"]
    idx = 0
    
    while True:
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.print("BEING ATTACKED?")
        brain.screen.set_cursor(2, 1)
        brain.screen.print("< " + options[idx] + " >")
        brain.screen.set_cursor(4, 1)
        brain.screen.print("L/R:Nav CHK:Sel")
        
        btn = wait_for_button_click()
        if btn == "LEFT":
            idx = (idx - 1) % len(options)
        elif btn == "RIGHT":
            idx = (idx + 1) % len(options)
        elif btn == "CHECK":
            return options[idx]

def select_uno_card_from_deck():
    colors = ["Red", "Yellow", "Green", "Blue", "Wild"]
    color_idx = 0
    
    while True:
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.print("TABLE TOP COLOR:")
        brain.screen.set_cursor(2, 1)
        brain.screen.print("< " + colors[color_idx] + " >")
        brain.screen.set_cursor(4, 1)
        brain.screen.print("L/R:Nav CHK:Sel")
        
        btn = wait_for_button_click()
        if btn == "LEFT":
            color_idx = (color_idx - 1) % len(colors)
        elif btn == "RIGHT":
            color_idx = (color_idx + 1) % len(colors)
        elif btn == "CHECK":
            selected_color = colors[color_idx]
            break

    if selected_color == "Wild":
        wild_options = ["Wild", "Wild Draw 4"]
        w_idx = 0
        while True:
            brain.screen.clear_screen()
            brain.screen.set_cursor(1, 1)
            brain.screen.print("TABLE WILD TYPE:")
            brain.screen.set_cursor(2, 1)
            brain.screen.print("< " + wild_options[w_idx] + " >")
            brain.screen.set_cursor(4, 1)
            brain.screen.print("L/R:Nav CHK:Sel")
            
            btn = wait_for_button_click()
            if btn == "LEFT":
                w_idx = (w_idx - 1) % len(wild_options)
            elif btn == "RIGHT":
                w_idx = (w_idx + 1) % len(wild_options)
            elif btn == "CHECK":
                card_res = choose_wild_color(wild_options[w_idx])
                display_card_graphic(card_res)
                wait(800, MSEC)
                return card_res
    else:
        values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Reverse", "Draw 2"]
        val_idx = 0
        while True:
            brain.screen.clear_screen()
            brain.screen.set_cursor(1, 1)
            brain.screen.print("TABLE TOP VALUE:")
            brain.screen.set_cursor(2, 1)
            brain.screen.print("< " + values[val_idx] + " >")
            brain.screen.set_cursor(4, 1)
            brain.screen.print("L/R:Nav CHK:Set")
            
            btn = wait_for_button_click()
            if btn == "LEFT":
                val_idx = (val_idx - 1) % len(values)
            elif btn == "RIGHT":
                val_idx = (val_idx + 1) % len(values)
            elif btn == "CHECK":
                card_res = selected_color + " " + values[val_idx]
                display_card_graphic(card_res)
                wait(800, MSEC)
                return card_res

def is_valid_play(card, top_discard):
    card_parts = card.strip().split(" ")
    target_parts = top_discard.strip().split(" ")

    card_color = card_parts[0]
    target_color = target_parts[0]

    card_val = " ".join(card_parts[1:])
    target_val = " ".join(target_parts[1:])

    if "Wild" in top_discard:
        return (card_color == target_color) and ("Wild" not in card)

    if "Wild" in card:
        return True

    return (card_color == target_color) or (card_val == target_val)

def process_player_turn(hand, deck, top_discard, new_cards_counter):
    while True:
        playable_indices = []
        for idx, card in enumerate(hand):
            if is_valid_play(card, top_discard):
                playable_indices.append(idx)

        actions = ["PLAY CARD", "DRAW CARD", "VIEW HAND"]
        action_idx = 0 if len(playable_indices) > 0 else 1

        while True:
            brain.screen.clear_screen()
            brain.screen.set_cursor(1, 1)
            brain.screen.print("TOP: " + shorten_card(top_discard))
            brain.screen.set_cursor(2, 1)
            brain.screen.print("< " + actions[action_idx] + " >")
            brain.screen.set_cursor(3, 1)
            brain.screen.print("Valid in Hand:" + str(len(playable_indices)))
            brain.screen.set_cursor(5, 1)
            brain.screen.print("L/R:Nav CHK:Sel")

            btn = wait_for_button_click()
            if btn == "LEFT":
                action_idx = (action_idx - 1) % len(actions)
            elif btn == "RIGHT":
                action_idx = (action_idx + 1) % len(actions)
            elif btn == "CHECK":
                selected_action = actions[action_idx]

                if selected_action == "VIEW HAND":
                    print_hand_to_screen(hand, "CHK: Return Menu")
                    break

                if selected_action == "PLAY CARD":
                    if len(playable_indices) == 0:
                        brain.screen.clear_screen()
                        brain.screen.set_cursor(1, 1)
                        brain.screen.print("NO MATCHING CARD")
                        brain.screen.set_cursor(2, 1)
                        brain.screen.print("FOR " + shorten_card(top_discard))
                        brain.screen.set_cursor(4, 1)
                        brain.screen.print("CHK: Must Draw")
                        wait_for_button_click()
                        action_idx = 1
                    else:
                        card_pos = 0
                        while True:
                            c_idx = playable_indices[card_pos]
                            c_card = hand[c_idx]

                            brain.screen.clear_screen()
                            brain.screen.set_cursor(1, 1)
                            brain.screen.print("TOP: " + shorten_card(top_discard))
                            brain.screen.set_cursor(2, 1)
                            brain.screen.print("HAND: " + shorten_card(c_card))
                            brain.screen.set_cursor(4, 1)
                            brain.screen.print("L/R:Nav CHK:Play")

                            c_btn = wait_for_button_click()
                            if c_btn == "LEFT":
                                card_pos = (card_pos - 1) % len(playable_indices)
                            elif c_btn == "RIGHT":
                                card_pos = (card_pos + 1) % len(playable_indices)
                            elif c_btn == "CHECK":
                                drive_to_center()

                                played_card = hand.pop(c_idx)
                                if "Wild" in played_card:
                                    wild_type = "Wild Draw 4" if "Wild Draw 4" in played_card else "Wild"
                                    played_card = choose_wild_color(wild_type)
                                    
                                # Display played card face-up as soon as center is reached
                                display_card_graphic(played_card)

                                print("Played Card Delivered to Center: " + played_card)
                                wait(1500, MSEC)

                                # Cover graphic before driving back
                                draw_card_full_screen("BACK", "")
                                drive_back_to_player()
                                return played_card

                if selected_action == "DRAW CARD":
                    drive_to_center()
                    flash_card_back_once()

                    drawn_card = draw_card(deck)
                    if drawn_card != None:
                        hand.append(drawn_card)
                        new_cards_counter[0] += 1
                        print("Drawn Card into Hand: " + drawn_card)
                    else:
                        brain.screen.clear_screen()
                        brain.screen.set_cursor(2, 1)
                        brain.screen.print("DECK EMPTY!")
                        wait(1500, MSEC)
                        
                    drive_back_to_player()
                    print_hand_to_screen(hand, "Drawn! CHK:Next")
                    return top_discard

# Main Program Execution Loop
def main_game_loop():
    uno_deck = create_shuffled_uno_deck()
    player_hand = start_game(uno_deck)
    new_cards_counter = [0]
    top_discard = "Red 0"
    
    while True:
        if len(player_hand) == 0:
            brain.screen.clear_screen()
            brain.screen.set_cursor(2, 1)
            brain.screen.print("YOU WIN UNO!")
            break

        print_hand_to_console(player_hand)
        print_hand_to_screen(player_hand, "CHK: Start Turn")

        attack_type = check_attack_status()
        
        if attack_type == "DRAW +2":
            print("Robot attacked with +2! Forcing 2 card draws...")
            drive_to_center()
            for _ in range(2):
                flash_card_back_once()
                c = draw_card(uno_deck)
                if c != None:
                    player_hand.append(c)
                    new_cards_counter[0] += 1
                    print("Attacked Draw: " + c)
            drive_back_to_player()
            print_hand_to_console(player_hand)
            print_hand_to_screen(player_hand, "+2 Drawn CHK:End")

        elif attack_type == "DRAW +4":
            print("Robot attacked with +4! Forcing 4 card draws...")
            drive_to_center()
            for _ in range(4):
                flash_card_back_once()
                c = draw_card(uno_deck)
                if c != None:
                    player_hand.append(c)
                    new_cards_counter[0] += 1
                    print("Attacked Draw: " + c)
            drive_back_to_player()
            print_hand_to_console(player_hand)
            print_hand_to_screen(player_hand, "+4 Drawn CHK:End")

        else:
            top_discard = select_uno_card_from_deck()
            print("Current Discard Top: " + top_discard)
            top_discard = process_player_turn(player_hand, uno_deck, top_discard, new_cards_counter)
            print_hand_to_console(player_hand)

        wait(300, MSEC)

# Start UNO Game
main_game_loop()