# https://www.hackerrank.com/challenges/strange-advertising/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def viralAdvertising(n):
    out = 2
    share = 5
    like = 2
    for i in range(1, n):
        shar = like * 3
        like = int(shar / 2)
        out = out + like
    return out

print(viralAdvertising(5))