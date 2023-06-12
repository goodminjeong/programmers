def solution(array, height):
    answer = 0
    for ar in array:
        if ar > height:
            answer += 1
    return answer


print(solution([149, 180, 192, 170], 167))
print(solution([180, 120, 140], 190))

# 출력화면
# 3
# 0