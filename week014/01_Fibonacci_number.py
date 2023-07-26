"""
피보나치 수

<문제 설명>
- 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.
- 예를들어
    F(2) = F(0) + F(1) = 0 + 1 = 1
    F(3) = F(1) + F(2) = 1 + 1 = 2
    F(4) = F(2) + F(3) = 1 + 2 = 3
    F(5) = F(3) + F(4) = 2 + 3 = 5
    와 같이 이어집니다.
- 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

<제한사항>
- n은 2 이상 100,000 이하인 자연수입니다.
"""
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from func_speed import func_speed


def fibonacci(n):
    if n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    a, b = 1, 1
    for _ in range(1, n):
        a, b = b, a + b
    return a


@func_speed
def solution(n):
    answer = fibonacci(n) % 1234567
    return answer


solution(52)
solution(5251)
solution(94251)
