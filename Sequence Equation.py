# https://www.hackerrank.com/challenges/permutation-equation/problem?h_r=next-challenge&h_v=zen


def permutationEquation(p):
    y = list()
    for x in range(1, len(p) + 1):
        for i in range(len(p)):
            if x == p[i]:
                px = i + 1
                break
        for j in range(len(p)):
            if px == p[j]:
                y.append(j + 1)
    return y

p = [5, 2, 1, 3, 4]
print(permutationEquation(p))