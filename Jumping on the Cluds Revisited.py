# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def jumpingOnClouds(c, k):
    i = 0
    e = 100
    while(True):
        e = e - 1
        i = (i + k) % len(c)
        if c[i] == 1:
            e = e - 2
        if i == 0:
            break
    return e
        


c = [0, 0, 1, 0, 0, 1, 1, 0]
k = 2
print(jumpingOnClouds(c, k))