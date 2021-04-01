# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def beautifulDays(i, j, k):
    count = 0
    for p in range(i, j + 1):
        diff = p - int(str(p)[::-1])
        if diff % k == 0:
            count = count + 1
    return count

i = 20
j = 23
k = 6
print(beautifulDays(i, j, k))