def epoch(j, m):
    global x, w, B, theta, t, rows
    weight_changes=0
    y=B
    for i in range(m):
        print(x[j][i],end=" ")
        y=y+x[j][i]*w[i]
    print("\t",1," ", y, end="  ")
    if(y>theta):
        y=1
    elif(y<theta and y>-theta):
        y=theta
    else:
        y=-1
    print(y,end="  ")
    print(t[j],end="\t\t")
    if y == t[j]:
        #No weight changes
        weight_changes=-1
        for i in range(m):
            print(0,end=" ")
        print(0,end=" ")
    else:
        for i in range(m):
            print(x[j][i]*t[j], end=" ")
            w[i]=w[i]+x[j][i]*t[j]
        B=B+t[j]
        print(t[j],end=" ")
    print("\t",end="")
    for i in range(m):
        print(w[i],end=" ")
    print(B)
    return weight_changes
        
if __name__ == "__main__":
    B=0
    theta=0
    rows, cols = (4, 2)
    value=int(rows)
    w = [0]*cols
    x = [[1,1],[-1,1],[1,-1],[-1,-1]]
    t = [1, -1, -1, -1]
    stop=1
    while value>0:
        print("Epoch ",stop)
        print("X \t B  yin  y  t  \tWeight changes \tWeights")
        for i in range(4):
            value+=epoch(i,cols)
        stop+=1
