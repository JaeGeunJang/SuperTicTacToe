board = [[0 for i in range (9)] for k in range (9)]
winstate = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

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
    for i in range (8) :
        if board[num][winstate[i][0]] == board[num][winstate[i][1]] == board[num][winstate[i][2]] :
            if board[num][winstate[i][0]] != 0 :
                print(winstate[i])
                return board[num][winstate[i][0]]


def main() :
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
