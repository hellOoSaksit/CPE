board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
count = None
def printBoard(board):
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

def insertplayer(Player,count):
    try:
        pos = int(input("Please insert your position: "))
        if (pos in range (0,9) and board[pos] == pos):
            board[pos] = Player
        else:
            print("The position you entered is not valid. Please try again.")
    except:
        print("An error occurred. Please try again.")
    if check_win(board) and count >= 0 and count <= 8:
        printBoard(board)
        print(f"Congratulations! {Player} has won the game!")
        return
    if count == 9:
        printBoard(board)
        print("It's a tie!")
        return
    if (Player == "X"): Player = "O"
    elif (Player == "O"): Player = "X"
    count += 1
    playgame(Player,count)

def check_win(board):
    # ตรวจสอบแถว
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2]:
            return True
    # ตรวจสอบคอลัมน์
    for i in range(3):
        if board[i] == board[i+3] == board[i+6]:
            return True
    # ตรวจสอบเส้นทแยงมุม
    if board[0] == board[4] == board[8]:
        return True
    elif board[2] == board[4] == board[6]:
        return True
    # No winner yet
    return False
            
def playgame(Player,count):
    printBoard(board)
    print ("Round : " , count)
    print("Player : " , Player)
    insertplayer(Player,count)
if __name__ == "__main__":
    playgame("X",1)
