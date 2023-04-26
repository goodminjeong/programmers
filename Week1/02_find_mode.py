def solution(array):
    answer = 0
    check = {}
    for ar in array:        # array에서 하나씩 돌아라
        if not ar in check:  # check 딕셔너리의 키값에 ar이 없으면
            check[ar] = 1   # check 딕셔너리의 키값이 ar인 곳에 value로 1을 넣어라
        else:
            check[ar] += 1  # 만약 키로 ar이 있으면 밸류로 +1 하라

    # check 딕셔너리를 가져와서 밸류값을 기준으로 내림차순 정렬
    sorted_check = sorted(check.items(), reverse=True,
                          key=lambda item: item[1])
    if len(sorted_check) > 1:
        if sorted_check[0][1] != sorted_check[1][1]:
            answer = sorted_check[0][0]
        else:
            answer = -1
    else:
        answer = sorted_check[0][0]
    return answer


array1 = [1, 2, 3, 3, 3, 4]
array2 = [1, 1, 2, 2]
array3 = [1]

print(solution(array1))
print(solution(array2))
print(solution(array3))
