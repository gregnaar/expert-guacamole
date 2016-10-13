import os
import random
os.system('cls' if os.name == 'nt' else 'clear')
board = [" "," "," "," "," "," "," "," "," "]
 
def update_board ():
    print(" -----------")
    print("|" , board[0], "|" , board[1] , "|", board[2] , "|")
    print(" -----------")
    print("|" , board[3], "|" , board[4] , "|" , board[5] ,"|")
    print(" -----------")
    print("|" , board[6], "|" , board[7] , "|" , board[8] ,"|")
    print(" -----------")

def free_space():
    free_space = False
for y in board:
    value = y
    if value == "x" :
        free_space = False
        break
    elif value == "o": 
        free_space = False
        break
    elif value == " ": 
        free_space= True
        break
    else :
        free_space= True
        break


def choose_move():
    while free_space == True :
        user_choice = input("Where do you want to put x?(between 1-9) ")
        user_choice = int(user_choice)-1
        if ( int(user_choice) < 0 or int(user_choice) > 8 ) :
            print("no")
        elif board[int(user_choice)] == "x" or board[int(user_choice)] == "o"  :
            print("Not an empty space!")
        else :
            board[int(user_choice)] = "x"
            os.system('cls' if os.name == 'nt' else 'clear')
            return

def ai_move():
    while free_space == True :
        a = random.randint(0, 8) 
        if board[int(a)] == "x" or board[int(a)] == "o"  :
            a = random.randint(0, 8)
        else :
            board[int(a)] = "o"
            os.system('cls' if os.name == 'nt' else 'clear')
            break

def player_win():
    if board[0] == "x" and board[1] == "x" and board[2] == "x" :
        return True
    if board[3] == "x" and board[4] == "x" and board[5] == "x" :
        return True
    if board[6] == "x" and board[7] == "x" and board[8] == "x" :
        return True
    if board[0] == "x" and board[4] == "x" and board[8] == "x" :
        return True
    if board[2] == "x" and board[4] == "x" and board[6] == "x" :
        return True
    if board[0] == "x" and board[3] == "x" and board[6] == "x" :
        return True
    if board[1] == "x" and board[4] == "x" and board[7] == "x" :
        return True
    if board[2] == "x" and board[5] == "x" and board[8] == "x" :
        return True   
    else :
        return False

def player_loose():
    if board[0] == "o" and board[1] == "o" and board[2] == "o" :
        return True
    if board[3] == "o" and board[4] == "o" and board[5] == "o" :
        return True
    if board[6] == "o" and board[7] == "o" and board[8] == "o" :
        return True
    if board[0] == "o" and board[4] == "o" and board[8] == "o" :
        return True
    if board[2] == "o" and board[4] == "o" and board[6] == "o" :
        return True
    if board[0] == "o" and board[3] == "o" and board[6] == "o" :
        return True
    if board[1] == "o" and board[4] == "o" and board[7] == "o" :
        return True
    if board[2] == "o" and board[5] == "o" and board[8] == "o" :
        return True
    else :
        return False

def draw():
    draw = False
for y in board:
    value = y
    if value == "x" :
        def_draw = False
        break
    elif value == "o": 
        def_draw = False
        break
    elif value == " " :
        def_draw = False
        break
    else:
        def_draw = True

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_screen():
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~TICTACTOE~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
    ~~~~~~~~~~~~~created by: Simon Laura - Kovacs Adam~~~~~~~~~~~~\n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
    ~~~~~Controls: press 1-9 on your keyboard, then press Enter~~~\n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~[1][2][3]~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~[4][5][6]~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~[7][8][9]~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
    ''')
while True :
    start_space = input('Press Space and then Enter to start the Game!')
    if start_space == " " :
        break


start_screen()
while True :
    update_board()
    choose_move()
    update_board()
    if player_win() == True :
        print("\n    ~~~~~~~~ \n     <|GG|> \n    YOU WON\n    :):):):) \n    ~~~~~~~~\n")
        break
    if draw() == True :
        print("\n    ~~~~~~~~~ \n     <|GG|> \n    ITS A TIE\n    :|:|:|:|\n    ~~~~~~~~~\n")
        break
    clear_screen()
    ai_move()
    update_board()
    if player_loose() == True :
            print("\n    ~~~~~~~~~ \n     <|GG|> \n    YOU LOOSE\n    :(:(:(:(\n    ~~~~~~~~~\n")
            break
    clear_screen()
    player_win()


