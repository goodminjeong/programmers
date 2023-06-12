"""
정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.
"""


def solution(num, k):
    answer = 0
    num_list = list(map(int, str(num)))  # 정수형인 num을 리스트로 변환
    for number in num_list:             # 리스트가 된 num_list를 for문에 돌려 값을 하나씩 꺼냄
        answer += 1                     # for문을 한 번씩 돌 때마다 1을 더해줌->자릿수가 됨
        if k in num_list:               # num_list에 매개변수 k가 있는 경우
            if number == k:             # num_list 속 number와 k가 같으면
                return answer           # answer 반환(자릿수)
        else:                           # num_list에 매개변수 k가 없는 경우
            return -1                   # -1을 반환함


print(solution(29183, 2))
print(solution(232443, 4))
print(solution(123456, 7))

# 출력화면
# 1
# 4
# -1
