the_board = {
    '7':' ', '8':' ', '9':' ',
    '4':' ', '5':' ', '6':' ',
    '1':' ', '2':' ', '3':' '
}
board_keys = [key for key in the_board]

def draw_the_board(board):
    print(board['7'] + '|' + board['8'] + '|' +board['9'])
    print('-+-+-')

    print(board['4'] + '|' + board['5'] + '|' +board['6'])
    print('-+-+-')

    print(board['1'] + '|' + board['2'] + '|' +board['3'])
    print('-+-+-')

# draw_the_board()

def game():
    turn = 'X'
    count  = 0
    for i in range(10):
        draw_the_board(the_board)
        print("Қәзір " + turn + " -тің жүрісі. Қай жерге баратынызды санмен көрсетіңіз (1..9)")
        move = input()
        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1
        else:
            print("Кешіріңіз, бұл ұяшық толып қалған. Басқасын тандаңыз.")
            continue
        
        
        if count >= 5:
            if the_board['7'] == the_board['8'] == the_board['9'] != ' ':
                draw_the_board(the_board)
                print('\nОйын аяқталды!\n')
                print("Player " + turn + " won the game!")
                break

            if the_board['4'] == the_board['5'] == the_board['6'] != ' ':
                draw_the_board(the_board)
                print('\nОйын аяқталды!\n')
                print("Player " + turn + " won the game!")
                break

            if the_board['1'] == the_board['2'] == the_board['3'] != ' ':
                draw_the_board(the_board)
                print('\nОйын аяқталды!\n')
                print("Player " + turn + " won the game!")
                break

            if the_board['7'] == the_board['5'] == the_board['3'] != ' ':
                draw_the_board(the_board)
                print('\nОйын аяқталды!\n')
                print("Player " + turn + " won the game!")
                break

            if the_board['1'] == the_board['5'] == the_board['9'] != ' ':
                draw_the_board(the_board)
                print('\nОйын аяқталды!\n')
                print("Player " + turn + " won the game!")
                break

        if turn == 'X':
            turn = 'O'
        elif turn == 'O':
            turn = 'X'
        


        if count == 9:
            print("\nОйын аяқталды!\n")
            print("Тең болды!")

    restart = input('Ойынды қайта жүктейсіз бе?! y/n')
    if restart == 'y' or restart == 'Y':
        for key in board_keys:
            the_board[key] = ' '
        game()

if __name__ == '__main__':
    game()