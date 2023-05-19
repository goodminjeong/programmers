def solution(k, m, score):
    answer = 0
    score.sort()
    box = len(score) % m
    price = score[box::m]
    for i in price:
        answer += i * m
    return answer


print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))    # 8
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))  # 33
