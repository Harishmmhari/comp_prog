def solve(a, n):
    li=[]
    w=0
    for i in range(n):
        w=w+a[i]
        li.append(a[i])



def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    print(solve(a, n))


main()