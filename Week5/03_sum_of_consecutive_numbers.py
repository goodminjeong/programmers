def solution(num, total):
    answer = []
    if num % 2 == 1:
        center = total // num
        start = center - ((num - 1)//2)
        end = center+((num-1)//2)
        for i in range(start, end+1):
            answer.append(i)
    else:
        left = total // num
        start = left - ((num - 1)//2)
        end = left + ((num - 1)//2) + 1
        for i in range(start, end+1):
            answer.append(i)

    return answer


print(solution(3, 12))  # [3, 4, 5]
print(solution(5, 15))  # [1, 2, 3, 4, 5]
print(solution(4, 14))  # [2, 3, 4, 5]
print(solution(5, 5))   # [-1, 0, 1, 2, 3]
