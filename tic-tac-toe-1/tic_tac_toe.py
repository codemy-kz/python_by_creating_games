import random



def create_empty_board(board):
    board_keys = [key for key in board]
    for k in board_keys:
        board[k] = ' '

def draw_the_board(board):
    print(board['7'] + '|' + board['8'] + '|' +board['9'])
    print('-+-+-')

    print(board['4'] + '|' + board['5'] + '|' +board['6'])
    print('-+-+-')

    print(board['1'] + '|' + board['2'] + '|' +board['3'])
    print('-+-+-')

def check_winner(board):
    result = False
    if board['7'] == board['8'] == board['9'] != ' ':
        result  = True
    if board['4'] == board['5'] == board['6'] != ' ':
        result = True  
    if board['1'] == board['2'] == board['3'] != ' ':
        result = True
    if board['7'] == board['5'] == board['3'] != ' ':
        result = True
    if board['1'] == board['5'] == board['9'] != ' ':
        result = True
    if board['1'] == board['4'] == board['7'] != ' ':
        result = True
    if board['2'] == board['5'] == board['8'] != ' ':
        result = True
    if board['3'] == board['6'] == board['9'] != ' ':
        result = True
    
    return result

def check_move_input_data():
    value = input()
    try:
        value = int(value)
        if value >= 1 and value <= 9:
            return str(value)
        else:
            return False
    except ValueError:
        return False
        
        

def game(board):
    create_empty_board(board)
    turn = random.choice(['X', 'O'])
    count  = 0
    while count != 9:
        draw_the_board(board)
        print("Қәзір " + turn + " -тің жүрісі. Қай жерге баратынызды санмен көрсетіңіз (1..9)")
        move = check_move_input_data()
        if move:
            if board[move] == ' ':
                board[move] = turn
                count += 1
            else:
                print("Кешіріңіз, бұл ұяшық толып қалған. Басқасын тандаңыз.")
                continue
        else:
            print("1 мен 9-дың аралығындағы санды енгізу қажет!")
            continue
        
        if count >= 5:
            check = check_winner(board)
        
            if check:
                print(board)
                draw_the_board(board)
                message = '\nОйын аяқталды!\n' +  turn + ' ойыншы женімпаз болды!'
                print(message)
                break

        
        if count == 9:
            draw_the_board(board)
            print("\nОйын аяқталды!\n")
            print("Жеңімпаз анықталмады!")
            break    

        if turn == 'X':
            turn = 'O'
        elif turn == 'O':
            turn = 'X'
        

        

    

if __name__ == '__main__':

    the_board = {
        '7':' ', '8':' ', '9':' ',
        '4':' ', '5':' ', '6':' ',
        '1':' ', '2':' ', '3':' '
    }

    flRunning = True
    while flRunning:
        game(the_board)

        restart = input('Ойынды қайта жүктейсіз бе?! y/n ')
        if restart == 'y' or restart == 'Y':
            flRunning = True
        else:
            flRunning = False