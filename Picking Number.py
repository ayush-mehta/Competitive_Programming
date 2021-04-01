# https://www.hackerrank.com/challenges/picking-numbers/problem

def pickingNumbers(a):
    # Write your code here
    a.sort()
    l = list()
    k = list()
    n = len(a)
    for i in range(n):
        k = [a[i]]
        for j in range(n):
            if j == i:
                continue
            if abs(a[j] - a[i]) <= 1 and a[j] - a[i] >= 0:
                k.append(a[j])
        l.append(k)
    print(l)
    out = list()
    for m in l:
        out.append(len(m))
    print(max(out))
    return

a = [4, 6, 5, 3, 3, 1]
pickingNumbers(a)