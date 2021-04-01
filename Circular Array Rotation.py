# https://www.hackerrank.com/challenges/circular-array-rotation/problem

def circularArrayRotation(a, k, queries):
    out = list()
    if k > len(a):
        k = k % len(a)
    a = a[-k:] + a[:-k]
    for query in queries:
        out.append(a[query])
    return out

a = [1, 2, 3]
k = 4
q = [0, 1, 2]
print(circularArrayRotation(a, k, q))
