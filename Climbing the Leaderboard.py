def find_rank(scores):
    ranks = list()
    r = 1
    for i in range(len(scores)):
        if i == 0:
            ranks = [1]
            continue
        if scores[i] != scores[i - 1]:
            r = r + 1
            ranks.append(r)
        else:
            ranks.append(r)
    return ranks
                



def climbingLeaderboard(ranked, player):
    # Write your code here
    # for score in player:
    #     for i in range(len(ranked)):
    #         if score >= ranked[i]:
    #             ranked[i] = score
    #             ranks = find_rank(ranked)
    #             print(ranks[i])
    #             break
    #         elif score < ranked[len(ranked) - 1]:
    #             ranks = find_rank(ranked)
    #             print(ranks[len(ranked) - 1] + 1)
    #             break

    ranks = find_rank(ranked)
    for score in player:
        for i in range(len(ranked)):
            if score >= ranked[i]:
                out = ranks[i]
                break
            elif score < ranked[len(ranked) - 1]:
                out = ranks[len(ranked) - 1] + 1
                break
        print(out)

    return

ranked = [100, 100, 50, 40, 20, 10]
player = [5, 25, 50, 120]
climbingLeaderboard(ranked, player)
