# https://www.hackerrank.com/challenges/library-fine/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

ef libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        fine = 10000
    elif y1 < y2:
        fine = 0
    elif m1 > m2:
        fine = 500 * abs(m2 - m1)
    elif m1 < m2 and y1 == y2:
        fine = 0
    elif d1 > d2 and m1 == m2 and y1 == y2:
        fine = 15 * (d1 - d2)
    else:
        fine = 0
    return fine


d1 = 9 
m1 = 6 
y1 = 2015

d2 = 6 
m2 = 6 
y2 = 2015

print(libraryFine(d1, m1, y1, d2, m2, y2))