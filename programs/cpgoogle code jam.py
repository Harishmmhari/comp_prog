def solve(a, n):
    li = []
    w = 0
    i=0
    for k in range(n):
        w = w + a[i]
        i=i+1
        li.append(a[i])
        i= i + 1
    print(li,w)
    print(min(li)*w)

def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    print(solve(a, n))


main()