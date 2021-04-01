# https://www.hackerrank.com/challenges/cut-the-sticks/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def cutTheSticks(arr):
    out = []
    j = 0
    arr = [arr]
    while(arr[j]):
        cut = min(arr[j])
        cuts = 0
        temp = []
        for i in range(len(arr[j])):
            if arr[j][i] >= cut:
                cuts = cuts + 1
            if arr[j][i] - cut > 0:
                temp.append(arr[j][i] - cut)
        arr.append(temp)
        out.append(cuts)
        j = j + 1
            
    return out




arr = [1, 2, 3, 4, 3, 3, 2, 1]
print(cutTheSticks(arr))