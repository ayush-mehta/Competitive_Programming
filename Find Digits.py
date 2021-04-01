# https://www.hackerrank.com/challenges/find-digits/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def findDigits(n):
    out = 0
    for i in str(n):
        i = int(i)
        if i == 0:
            continue
        if n % i == 0:
            out = out + 1
    return out

n = 1012
print(findDigits(n))