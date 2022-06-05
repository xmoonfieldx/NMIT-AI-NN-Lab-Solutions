import random
def check_victory(board,p,pos):
    if(board[0]==p and board[1]==p and board[2]==p):
        print("Player",p, "has won")
        return 1
    elif(board[0]==p and board[3]==p and board[6]==p):
        print("Player",p, "has won")
        return 1
    elif(board[1]==p and board[4]==p and board[7]==p):
        print("Player",p, "has won")
        return 1
    elif(board[2]==p and board[5]==p and board[8]==p):
        print("Player",p, "has won")
        return 1
    elif(board[3]==p and board[4]==p and board[5]==p):
        print("Player",p, "has won")
        return 1
    elif(board[6]==p and board[7]==p and board[8]==p):
        print("Player",p, "has won")
        return 1
    elif(board[2]==p and board[4]==p and board[6]==p):
        print("Player",p, "has won")
        return 1
    elif(board[0]==p and board[4]==p and board[8]==p):
        print("Player",p, "has won")
        return 1
    
    
if __name__ == "__main__":
    win=0
    print('Welcome to Tic Tac Toe!')
    times=0
    p1="X"
    p2="O"
    print("This is what the board looks like at the moment.")
    board=['_','_','_','_','_','_','_','_','_']
    i=0
    times=0
    for x in range(3):
        for x in range(3):
            print(board[i],end=" ")
            i+=1
        print(end="\n")
    print(end="\n\n\n")
    turn=0
    while True:
        if(turn==0):
            print("Player X:")
            y=random.randint(1, 9)
            if(board[y-1] == "_"):
                board[y-1]=p1
                i=0
                times+=1
                turn=1
                for x in range(3):
                    for x in range(3):
                        print(board[i],end=" ")
                        i+=1
                    print(end="\n")
                print(end="\n\n\n")
            else:
                print("The spot is occupied.")
                turn=0
                continue
        
        win = check_victory(board,p1,y-1)
        if(win==1):
            break
        if(times==9):
            print("This was a draw.")
            break      
        else:
            print("Player O:")
            y=random.randint(1, 9)
            if(board[y-1] == "_"):
                board[y-1]=p2
                i=0
                times+=1
                turn=0
                for x in range(3):
                    for x in range(3):
                        print(board[i],end=" ")
                        i+=1
                    print(end="\n")
                print(end="\n\n\n")
            else:
                print("The spot is occupied.")
                turn=1
                continue
            win = check_victory(board,p2,y-1)
        if(win==1):
            break
