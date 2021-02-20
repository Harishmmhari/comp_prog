def solve(a,n):
    n=n-1
    key=a[n]

    while(1):
        if len(a) <= n + 1:
            return -1
            break

        if key < a[n+1]:
            if sumd(key) > sumd(a[n+1]):

                return n+2
            else:
                pass
        else:
            pass
        n = n + 1




def sumd(num):
    su = 0
    for digit in str(num):
        su += int(digit)

    return su

def main():
    n,q=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    print(n,q,a)
    for i in range(q):
        num=int(input())
        k=solve(a,num)
        print(k)
    exit()
main()