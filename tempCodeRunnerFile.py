def solution(lottos, win_nums):
    answer = []
    zero, correct = 0, 0
    ranking = {2: 5, 3: 4, 4: 3, 5: 3, 6: 1}

    for lotto in lottos:
        if lotto == 0:
            zero += 1
        if lotto in win_nums:
            correct += 1

    highest_ranking = ranking[correct + zero]
    try:
        lowest_ranking = ranking[correct]
    except:
        lowest_ranking = 6

    answer.append(highest_ranking)
    answer.append(lowest_ranking)

    return answer