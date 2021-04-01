# https://www.hackerrank.com/challenges/save-the-prisoner/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def saveThePrisoner(n, m, s):
    if m % n != 0:
        var = (m % n) + s - 1
    else:
        var = n + s - 1
    if var > n:
        var = var - n
    return var

n = 7
m = 21
s = 7
print(saveThePrisoner(n, m, s))