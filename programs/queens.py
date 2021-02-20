def add(nn):
    global m
    global n
    global hi

    hi=[]
    n=nn
    global total
    total=0
    m = []
    for j in range(n):
        k = []
        for p in range(n):
            k.append(0)
        m.append(k)

    solve()
def check(x,y):

    global m
    n=len(m)
    for i in range(n):
        if m[i][y]==1:
            return False
        if m[x][i]==1:
            return False
    for j in range(1,n):
        x1=x+j
        y1=y+j
        x2=x-j
        y2=y-j
        if x1<n and y1<n :
            if m[x1][y1]==1:
                return False
        if x2>=0 and y2>=0:
            if m[x2][y2]==1:
                return False
        if x1<n and y2>=0 :
            if m[x1][y2]==1:
                return False
        if 0<=x2<n and n>y1>=0:
            if m[x2][y1]==1:
                return False

    return True
def check2(m):
    global hi

    if m in hi:

        return False
    return True
def check1():
    global m
    global n
    global total
    global hi

    sum=0
    for j in range(n):
        for p in range(n):
            sum=sum+m[p][j]
    if sum==n and check2(m):

        hi.append(m)

        total=total+1
    return


def solve():
    global m
    global n
    global str

    for x in range(n):
        for y in range(n):
            if m[x][y]==0:
                if check(x, y):
                    m[x][y] = 1
                    print(x,y,m)
                    solve()
                    m[x][y] = 0
                else:
                    m[x][y] = 2
                    solve()

    str.append(m)
    return

global str
str=[]
add(5)
print(len(str))
global total,hi
print(total,hi)

