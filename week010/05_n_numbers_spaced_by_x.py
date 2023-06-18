"""
x만큼 간격이 있는 n개의 숫자

<문제 설명>
- 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 
- 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

<제한 조건>
- x는 -10000000 이상, 10000000 이하인 정수입니다.
- n은 1000 이하인 자연수입니다.
"""
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from func_speed import func_speed


@func_speed
def solution(x, n):
    answer = [x]
    for i in range(n - 1):
        answer.append(answer[i] + x)
    return answer


solution(2, 5)  # [2,4,6,8,10]
solution(4, 3)  # [4,8,12]
solution(-4, 2)  # [-4, -8]
solution(0, 3)  # [0, 0, 0]
solution(-10000000, 1000)
