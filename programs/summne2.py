import os
def fac(arr, k):
    for i in arr:
        if (k % i == 0):
            continue
        else:
            return False
    return True


def check(n, arr):
    for i in arr:
        if i % n == 0:
            pass
        else:
            return False
    return True


def getTotalX(a, b):
    # Write your code here

    i = []
    for k in range(max(a), min(b) + 1):
        if fac(a, k):
            i.append(k)

    # print(i)
    jp = []

    for m in i:
        if check(m, b):
            jp.append(m)
    print(jp)
    return (len(jp))


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    #fptr.write(str(total) + '\n')

    #fptr.close()