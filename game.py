import random

mode = int(input("Do you want to play single player or duo(1 or 2): "))
if mode == 1:
    board = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

    board_keys = []

    for key in board:
        board_keys.append(key)

    def printboard(board):
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['1'] + '|' + board['2'] + '|' + board['3'])

    def g1():
        count = 0
        user = 'X'
        ai = 'O'

        for i in range(10):
            printboard(board)
            if count % 2 == 0:
                print("Its your turn")

                move = input()

                if board[move] == ' ':
                    board[move] = user
                    count+=1
                else:
                    print("That spot has already been taken")
                    continue
            if count % 2 != 0:
                while True:
                    x = str(random.randint(1, 9))
                    if board[x] == ' ':
                        board[x] = ai
                        count+=1
                        break

            if count >= 5:
                if board['7'] == board['8'] == board['9'] != ' ':
                    printboard(board)
                    print("\nGame Over")
                    print(board['7'] + " wins")
                    break
                elif board['4'] == board['5'] == board['6'] != ' ':
                    board(board)
                    print("\nGame Over")
                    print(board['4'] + " wins")
                    break
                elif board['1'] == board['2'] == board['3'] != ' ':
                    printboard(board)
                    print("\nGame Over")
                    print(board['1'] + " wins")
                    break
                elif board['1'] == board['4'] == board['7'] != ' ':
                    printboard(board)
                    print("\nGame Over")
                    print(board['1'] + " wins")
                    break
                elif board['2'] == board['5'] == board['8'] != ' ':
                    printboard(board)
                    print("\nGame Over")
                    print(board['2'] + " wins")
                    break
                elif board['3'] == board['6'] == board['9'] != ' ':
                    printboard(board)
                    print("\nGame Over")
                    print(board['3'] + " wins")
                    break
                elif board['7'] == board['5'] == board['3'] != ' ':
                    printboard(board)
                    print("\nGame Over")
                    print(board['7'] + " wins")
                    break
                elif board['1'] == board['5'] == board['9'] != ' ':
                    printboard(board)
                    print("\nGame Over")
                    print(board['1'] + " wins")
                    break

            if count == 9:
                print("\nGame Over")
                print("It's a Tie")

        restart = input("Do want to play Again?(y/n)")
        if restart.lower() == "y":
            for key in board_keys:
                board[key] = " "

            g1()

    if __name__ == "__main__":
        g1()

if mode == 2:
    board = {'7': ' ' , '8': ' ' , '9': ' ' ,
             '4': ' ' , '5': ' ' , '6': ' ' ,
             '1': ' ' , '2': ' ' , '3': ' ' }

    board_keys = []

    for key in board:
        board_keys.append(key)

    def printboard(board):
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['1'] + '|' + board['2'] + '|' + board['3'])

    def g2():

        turn = 'X'
        count = 0

        for i in range(10):
            printboard(board)
            print("It's your turn, " + turn)

            move = input()

            if board[move] == ' ':
                board[move] = turn
                count += 1
            else:
                print("That spot has already been taken")
                count-=1
                continue

            if count >= 5:
                if board['7'] == board['8'] == board['9'] != ' ':
                    printboard(board)
                    print("\nGame Over")
                    print(turn + " won")
                    break
                elif board['4'] == board['5'] == board['6'] != ' ':
                    board(board)
                    print("\nGame Over")
                    print(turn + " won")
                    break
                elif board['1'] == board['2'] == board['3'] != ' ':
                    printboard(board)
                    print("\nGame Over")
                    print(turn + " won")
                    break
                elif board['1'] == board['4'] == board['7'] != ' ': 
                    printboard(board)
                    print("\nGame Over.\n")
                    print(turn + " won")
                    break
                elif board['2'] == board['5'] == board['8'] != ' ': 
                    printboard(board)
                    print("\nGame Over")
                    print(turn + " won")
                    break
                elif board['3'] == board['6'] == board['9'] != ' ': 
                    printboard(board)
                    print("\nGame Over")
                    print(turn + " won")
                    break
                elif board['7'] == board['5'] == board['3'] != ' ':
                    printboard(board)
                    print("\nGame Over")
                    print(turn + " won")
                    break
                elif board['1'] == board['5'] == board['9'] != ' ': 
                    printboard(board)
                    print("\nGame Over")
                    print(turn + " won")
                    break

            if count == 9:
                print("\nGame Over")
                print("It's a Tie")

            if turn =='X':
                turn = 'O'
            else:
                turn = 'X'

        restart = input("Do want to play Again?(y/n)")
        if restart.lower() == "y":
            for key in board_keys:
                board[key] = " "

            g2()

    if __name__ == "__main__":
        g2()
