# https://www.hackerrank.com/challenges/append-and-delete/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def appendAndDelete(s, t, k):
    for i in range(len(s)) :
        if i >= len(t) or s[i] != t[i]:
            break
    if i == len(s) - 1:
        i = i + 1
    operation = len(s[i:])
    if i >= len(t):
        if k >= operation:
            out = 'Yes'
        else:
            out = 'No'
    else:
        operation = operation + len(t[i:])
        if k >= operation:
            out = 'Yes'
        else:
            out = 'No'
    if (k - operation < 2 * len(t) and (k - operation) % 2 != 0) and k > operation and i != 0:
        out = 'No'
    return out


s = 'abcd'
t = 'abcdert'
k = 10
print(appendAndDelete(s, t, k))