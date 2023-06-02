def solution(lottos, win_nums):
    answer = []
    zero, correct = 0, 0
    ranking = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}

    for lotto in lottos:
        if lotto == 0:
            zero += 1
        elif lotto in win_nums:
            correct += 1

    highest_ranking = ranking[correct + zero]
    lowest_ranking = ranking[correct]

    answer.append(highest_ranking)
    answer.append(lowest_ranking)

    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 0], [20, 9, 3, 45, 4, 35]))
print(solution([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]))
print(solution([1, 2, 3, 4, 0, 12], [7, 8, 9, 10, 11, 12]))
