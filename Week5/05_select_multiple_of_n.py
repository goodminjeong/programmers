def solution(n, numlist):
    answer = []
    for num in numlist:
        if (num % n) == 0:
            answer.append(num)
    return answer


print(solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12]))  # [6, 9, 12]
print(solution(5, [1, 9, 3, 10, 13, 5]))    # [10, 5]
print(solution(12, [2, 100, 120, 600, 12, 12]))  # [120, 600, 12, 12]
