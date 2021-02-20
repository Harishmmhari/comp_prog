def add():
    global m
    m = [
        [8, 4, 3, 5, 6, 7, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 8, 4, 6, 7, 2, 0, 0, 0],
        [0, 0, 0, 1, 5, 9, 0, 0, 0],
        [0, 0, 0, 8, 3, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    k=solve()






def check(r, c, n):

    global m
    k = (r // 3)*3
    r1 = (c // 3)*3

    for i in range(0,3):
        for j in range(0,3):
            if n == m[k+i][r1+j]:
                return False

    for num in range(9):
        if n == m[r][num]:
            #print(1)
            return False
    for num1 in range(9):
        if n == m[num1][c]:
            #print(2)
            return False
    if (r==c):
        for t in range(9):
            if n==m[t][t]:
                #print(3)
                return False
    if (8-r==c):
        for t1 in range(9):
            if n==m[8-t1][t1]:
                #print(4)
                return False
    if ((0<=r+2<=8)and(0<=c+1<=8)):
        if m[r+2][c+1]==n:
            #print(5)
            return False
    if ((0<=r+2<=8)and(0<=c-1<=8)):
        if m[r+2][c-1]==n:
            #print(6)
            return False
    if ((0<=r-2<=8)and(0<=c+1<=8)):
        if m[r-2][c+1]==n:
            #print(7)
            return False
    if ((0<=r+2<=8)and(0<=c-1<=8)):
        if m[r+2][c-1]==n:
            #print(8)
            return False
    if ((0<=r+1<=8)and(0<=c+2<=8)):
        if m[r+1][c+2]==n:
            #print(9)
            return False
    if ((0<=r-1<=8)and(0<=c+2<=8)):
        if m[r-1][c+2]==n:
            #print(10)
            return False
    if ((0<=r+1<=8)and(0<=c-2<=8)):
        if m[r+1][c-2]==n:
            #print(11)
            return False
    if ((0<=r-1<=8)and(0<=c-2<=8)):
        if m[r-1][c-2]==n:
            #print(12)
            return False

    return True


def solve():
    global m
    '''if len(m)!= len(m[0]):
        print("matrix should be square")
    else:'''

    for row in range(9):
        for column in range(9):
            if m[row][column] == 0:
                for i in range(1, 10):
                    if check( row, column, i):
                        m[row][column] = i

                        solve()
                        m[row][column]=0
                return
    for i in m:
        print(i
              )
    input("more?")


add()