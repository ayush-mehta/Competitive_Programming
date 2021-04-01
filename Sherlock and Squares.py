# https://www.hackerrank.com/challenges/sherlock-and-squares/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import math


def squares(a, b):
    out = []
    for x in range(int(math.sqrt(a)), int(math.sqrt(b)) + 1):
        x2 = x * x
        if x2 >= a and x2 <= b:
            out.append(x2)
    return out
a = 17
b = 24
print(squares(a, b))