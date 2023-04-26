def solution(s1, s2):
    answer = 0
    for st in s1:
        if st in s2:
            answer += 1
    return answer


print(solution(['a', 'b', 'c'], ['com', 'b', 'd', 'p', 'c']))
print(solution(['n', 'omg'], ['m', 'dot']))


# 출력화면
# 2
# 0
