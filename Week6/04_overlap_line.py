def solution(lines):
    answer, cnt = 0, 0
    for i in range(len(lines)):
        globals()["line{}".format(i)] = [j for j in range(lines[i][0], lines[i][1]+1)]
    start = min(lines[0][0], lines[1][0], lines[2][0])
    end = max(lines[0][1], lines[1][1], lines[2][1])
    for i in range(start, end+1): 
        for j in range(len(lines)):
            if (i in globals()["line"+str(j)]) and (i+1 in globals()["line"+str(j)]):
                cnt += 1
        if cnt > 1:
            answer += 1
        cnt = 0
    return answer

print(solution([[0, 1], [2, 5], [3, 9]]))   # 2
print(solution([[-1, 1], [1, 3], [3, 9]]))  # 0
print(solution([[0, 5], [3, 9], [1, 10]]))  # 8