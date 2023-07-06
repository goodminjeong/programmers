"""
최대공약수와 최소공배수

<문제 설명>
- 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
- 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
- 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

<제한사항>
- 두 수는 1이상 1000000이하의 자연수입니다.
"""
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from func_speed import func_speed


# 첫 번째 풀이
@func_speed
def solution1(n, m):
    answer = []
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    for i in range(max(n, m), (n * m) + 1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break
    return answer


# 두 번째 풀이
@func_speed
def solution2(n, m):
    answer = []
    dn, dm = n, m
    while dm > 0:
        dn, dm = dm, dn % dm
    answer.append(dn)
    answer.append((n * m) // dn)
    return answer


solution1(3, 12)
solution1(2, 5)

solution2(3, 12)
solution2(2, 5)
