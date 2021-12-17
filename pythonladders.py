import random

# Codigo criado durante a aula de Fundamentos de Programação do dia 16/12/2021
# O CODIGO NÃO ESTÁ COMPLETO E PODERÁ TER BUGS! :)

def playerTag(pID):
    alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alfa[pID]

def buildboard():
    board = [0]*101
    ladders = {
        (1,38), (4,14), (9,31), (28, 84), (21, 42), (51, 67), (72,91), (80,99)
    }
    snakes = {
        (98, 79), (93, 73), (95, 75), (87, 36), (62, 19), (54, 34), (64, 60), (17, 7)
    }

    for i in range(0, len(board)):
        for l in ladders:
            if i == l[0]:
                board[i] = l
        for s in snakes:
            if i == s[0]:
                board[i] = s
    
    return board

def move_event(pos_end, player):
    player = pos_end
    return player

def roll_dice():
    val = 2 #random.randint(1,6)
    print("I Rolled a " + str(val))
    return val

def string_build(x, squareType):
    if len(x) < 2:
        return "|" + str(x) + "  - " + str(squareType) + "|"
    elif len(x) > 2:
        return "|" + str(x) + "- " + str(squareType) + "|"
    else:
        return "|" + str(x) + " - " + str(squareType) + "|"

def print_board(board, players, pID):
    print("You are here: " + str(player))
    pboard = ""
    for x in range(1, len(board)):
        
        # If number characters < 2 
        str_val = str(x)
        temp = set(players)
        if len(set(players)) != len(players) and x == players[pID]:
            pboard += "|" + str(x) 
            for pPos in range(0, len(players)-1):
                for pPos_aux in range(1, len(players)):
                    if players[pPos] == players[pPos_aux]:
                        pboard += "  - " + playerTag(pPos) + " " 
                        
            pboard += "|"

        elif x == players[pID]:
            pboard += string_build(str(x), playerTag(pID))

        elif type(board[x]) is tuple:
            if board[x][0] < board[x][1]:
                pboard += string_build(str(x), "L")
            elif board[x][0] > board[x][1]:
                pboard += string_build(str(x), "S")
        else:
            pboard += string_build(str(x), " ")

        if x % 10 == 0:
            pboard += "\n"
        
            
    print(pboard)

def initGame():
    print("State Number of Players (Min 1): ")
    num = input()
    num_player = [0] * int(num)
    return num_player


# Int Association
# 0 = Casa Normal
# (x,y) = Ladders, Snakes
# Ladders[0] = x
# Ladders[1] = y
board = buildboard()
running = True

while True:
    print("WELCOME TO PYTHONS AND LADDERS!!!!")
    print("Menu: ")
    print("1. Start Game")
    print("2. Exit")
    read_input = input()
    if read_input == str(1) :
        players = initGame()
        break
    elif read_input == str(2):
        exit()
    else:
        print("Invalid Option")

print("Game Starts Now!!!!")    
while True:
    pCounter = 0
    for player in players:
        print("Roll with \'r\'")
        player_input = input()

        if player_input == 'r':
            val = roll_dice()

            move_val = player + val

            if move_val < len(board):
                player = move_event(move_val, player)
                if player == len(board)-1:
                    print("YOU WIN!!!")
                    exit()
            elif move_val > len(board):
                new_pos = move_val - len(board)
                player = move_event(len(board)-new_pos, player)
                
            if board[player] != 0:
                player = move_event(board[player][1], player)


            
            print_board(board, players, pCounter)
        else:
            print("ERROR INPUT!")
            print("Please use \"r\"")
        
        players[pCounter] = player
        pCounter += 1


    



