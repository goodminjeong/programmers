def solution(arr1, arr2):
    answer = []
    # 답 행렬의 크기는 arr1의 행 개수(길이) x arr2의 열 개수(arr2[0] 길이)
    answer_row = len(arr1)  # 답 행렬의 행이 되는 개수
    answer_col = len(arr2[0])   # 답 행렬의 열이 되는 개수
    arr1_col_arr2_row = len(arr1[0])    # 답 행렬 요소에 더해지는 곱 개수
    # 행렬1의 행 개수만큼 돌리기
    for l in range(answer_row):
        # 답 행렬의 각 행 리스트 초기화
        sum_answer_row = [0 for _ in range(answer_col)]
        # 행렬2의 열 개수만큼 돌리기
        for n in range(answer_col):
            # 답 행렬 각 요소에 더해지는 곱의 개수만큼 돌리기
            for m in range(arr1_col_arr2_row):
                # 답 행렬 한 행의 n번째 열 += 행렬1 l행 m열 * 행렬2 m행 n열
                sum_answer_row[n] += (arr1[l][m] * arr2[m][n])
        # 한 행의 각 열이 다 채워지면 답 행렬에 붙이기
        answer.append(sum_answer_row)
    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])) # [[15, 15], [15, 15], [15, 15]]
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],
      [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))   # [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
