# https://www.hackerrank.com/challenges/utopian-tree/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def utopianTree(n):
    h = 0
    for i in range(60):
        if i % 2 == 0:
            h = h + 1
        else:
            h = h * 2
        if i == n:
            return h

n = 4
print(utopianTree(n))