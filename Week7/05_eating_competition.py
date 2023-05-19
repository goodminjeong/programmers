def solution(food):
    left = ''
    for i in range(1, len(food)):
        share = food[i] // 2
        left += str(i) * share
    right = "".join(sorted(left, reverse=True))
    # right = left[::-1] <- 더 간편하게 역순으로 바꾸는 방법..
    answer = left + "0" + right
    return answer


print(solution([1, 3, 4, 6]))   # 1223330333221
print(solution([1, 7, 1, 2]))   # 111303111
