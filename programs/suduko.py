m= [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]

        ]
total=100
def possible(x,y,n,num):
    global total
    x_sum=0
    y_sum=0
    for i in range(n):
        x_sum=x_sum+m[x][i]
        y_sum=y_sum+m[i][y]
    if x==n and y!=n:
        if x_sum<total:
            if num==total-x_sum:
                return True
            else:
                return False
        else:
            return False
    if y==n and x!=n:
        if y_sum<total:
            if num==total-y_sum:
                return True
            else:
                return False
        else:
            return False
    if y==n and x==n:
        if y_sum<total and x_sum<total:
            if num==total-y_sum and n==total-x_sum:
                return True
            else:
                return False
        else:
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
                for i in range(1, 20):
                    if possible(row,column,9,i):
                        m[row][column] = i

                        solve()
                        m[row][column]=0
                        print(m)
                return
    print(m)










