def pboard(board) :
    print("\n ------- ------- -------")
    for a in range (3) :
        for b in range (3) :
            print("|", end = " ")
            for c in range (3) :
                for d in range (3) :
                    if board[a*3+c][b*3+d] == 1 :
                        print("O", end = " ")
                    elif board[a*3+c][b*3+d] == -1 :
                        print("X", end = " ")
                    else :
                        print("-", end = " ")
                print("|", end = " ")
            print("")
        print(" ------- ------- -------")

def mboard(board,num) :
    for i in range (1,10) :
        if board[num-1][i-1] == 0 :
            print("--", end = " ")
        elif board[num-1][i-1] == 1 :
            print("O", end == " ")
        elif board[num-1][i-1] == -1 :
            print("X", end == " ")
        if i%3 == 0 :
            print("")

def inputGame(board, num, order) :
    o = order
    b = board
    while(True) :
        selec = input("Input the cell 1~9 \n(left-up = 1 and right-down = 9) : ")
        if selec not in ["1","2","3","4","5","6","7","8","9"] :
            print("Please input right number (1~9) : ")
        elif selec in ["1","2","3","4","5","6","7","8","9"] and b[num][int(selec)-1] != 0 :
            selec = int(selec) - 1
            print("That cell already fill. Please input another number : ")
        else :
            selec = int(selec) - 1
            b[num][selec] = order
            o = order*(-1)
            break
    return b, o, selec

def winGame(board,num) :
    for hori in range (3) :
        if board[num][hori*3] == board[num][hori*3+1] == board[num][hori*3+2] and board[num][hori*3] != 0 :
            print("horizon win")
            return board[num][hori*3]
        if board[num][hori*3] == board[num][hori+3] == board[num][hori+6] and board[num][hori*3] != 0 :
            print("Vertical win")
            return board[num][hori*3]
    if board[num][0] == board[num][4] == board[num][8] and board[num][0] != 0 :
        print("0 to 9 win")
        return board[num][0]
    if board[num][2] == board[num][4] == board[num][6] and board[num][2] != 0 :
        print("3 to 7 win")
        return board[num][0]


'''
def main() :
    board = [[0 for i in range (9)] for k in range (9)]
    tboard = [[i+k*10 for i in range (1,10)] for k in range (1,10)]

    num = 4
    order = 1
    while(True) :
        prenum = num
        pboard(board)
        board, order, num = inputGame(board ,num, order)
        win = winGame(board,prenum)
        if win != 0 :
            if win == -1 :
                print("Player2 win")
                break
            if win == 1 :
                print("Player 1 win")
                break

'''
