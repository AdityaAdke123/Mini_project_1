
def printBoard(board):

    for row in range(6, 0,-1):                                                         # Iterate over each row, from row 6 to 1
        print("-----------------------------------------------")

        print(f'| {row } ', end ='')                                                   # Print the row number and each column's content for the current row
        for col in range(7):

            print (f'| {board[row - 1][col]:^3}', end=' ')                             # Ensure consistent spacing for X, O, or empty spaces
        print('|')


    print ("-----------------------------------------------")
    print ('|R/C|  a  |  b  |  c  |  d  |  e  |  f  |  g  |')                          # Print the bottom border and column labels
    print ("-----------------------------------------------")



def reset() :                                                                          # Function to reset the game board with empty slots

    return [[' ' for _ in range(7)] for _ in range(6)]



def validate_Entry (board, col,row):                                                   # Function to verify if the player's move is valid

    if col < 0 or col > 6 or  row < 0 or row > 5:
        return False
    return board[row][col] == ' '



def CheckFull (board):                                                                  # Function to determine if the board is completely filled
    return all(board[5][col] != ' ' for col in range(7))



def AvailablePositions(board):                                                          # Function to get a list of the lowest available positions in each column
    available = []

    for col in range(7):
        for row in range(6):
            if board[row][col] == ' ':
                available.append((col, row))

                break
    return available



def checkWin(board, turn):                                                      # Function to check if a player has achieved a winning condition

    piece = 'X' if turn % 2 == 0 else 'O'

    # Check horizontally
    for row in range(6):
        for col in range(4):  # Only check where 4 in a row is possible horizontally
            if all(board[row][col + i] == piece for i in range(4)):
                return True

    # Check vertically
    for col in range(7):
        for row in range(3):  # Only check where 4 in a row is possible vertically
            if all(board[row + i][col] == piece for i in range(4)):
                return True

    # Check diagonally (bottom-left to top-right)
    for row in range(3):
        for col in range(4):
            if all(board[row + i][col + i] == piece for i in range(4)):
                return True

    # Check diagonally (top-left to bottom-right)
    for row in range(3, 6):
        for col in range(4):
            if all(board[row - i][col + i] == piece for i in range(4)):
                return True

    return False



def checkEnd(board, turn):                                                      # Function to check if the game is over, either by a win or a full board
    return CheckFull(board) or checkWin(board, turn)


def playGame():                                                                 # Set up the board and start the turn count at 0

    board = reset()
    turn = 0
    print('New game: X goes first.')


    while True:                                                                 # Continue the game loop until the game ends
        printBoard(board)                                                       # Determine the current player (X or O)

        current_player = 'X' if turn %2 ==  0 else 'O'
        print(f"{current_player}'s turn.")


        available = AvailablePositions(board)                                   # Display available positions
        formatted_positions = [f'{chr(97 + col)}{row + 1}' for col, row in available]

        print(f"Available positions are: {formatted_positions}")


        while True:                                                             # Ask the player for a move
            move = input("Please enter column-letter and row-number (e.g., a1): ").lower()

            if len(move) == 2 and move[0] in 'abcdefg' and move[1] in '123456':
                col = ord(move[0]) - 97  # Convert the column letter to a column index
                row = 6 - int(move[1])  # Convert the row number to a row index

                if validate_Entry(board, col, row):
                    break  # If valid, proceed with the move
            print("Invalid entry. Please try again.")


        for r in range(6):                                                       # Place the piece in the lowest available row in the selected column

            if board[r][col] == ' ':

                board[r][col] = current_player
                break

        print("Thank you for your selection.")


        if checkWin(board, turn):                                                # Check if the current player has won the game
            printBoard(board)
            print(f"{current_player} IS THE WINNER!!!")

            break


        if CheckFull(board):                                                      # Check for a tie game if the board is full
            printBoard(board)
            print("It's a tie!")

            break

        turn += 1

    if input('Another game (y/n)? ').lower() == 'y':
        playGame()

    else:
        print("Thank you for playing!")

playGame()
