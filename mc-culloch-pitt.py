def solve(result):
    global x, n
    for i in range(-6,6):
        for j in range(-6,6):
            sol = []
            for k in range(4):
                y=i*x[k][0]+j*x[k][1]
                if(y>=n):
                    sol.append(1)
                    #print(sol)
                else:
                    sol.append(0)
            if(sol==result):
                print(i, j)
                
if __name__ == "__main__":  
    n=int(input("Enter your thresold value: "))
    x=[[0,0],[0,1],[1,0],[1,1]]
    #AND function
    print("AND gate\nThe weights are: ")
    result=[0,0,0,1]
    solve(result)
    #OR function
    print("\nOR gate\nThe weights are: ")
    result=[0,1,1,1]
    solve(result)
    #ANDNOT function
    print("\nANDNOT gate\nThe weights are: ")
    result=[0,0,1,0]
    solve(result)
    #EXOR function
    print("\nEXOR gate\nThe weights are: ")
    x=[[0,0],[0,1],[1,0],[0,0]]
    result=[0,1,1,0]
    solve(result)
