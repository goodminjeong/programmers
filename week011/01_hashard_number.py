"""
하샤드 수

<문제 설명>
- 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
- 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
- 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

<제한 조건>
- x는 1 이상, 10000 이하인 정수입니다.
"""
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from func_speed import func_speed


@func_speed
def first(x):
    x_sum = sum(list(map(int, str(x))))
    if x % x_sum != 0:
        return False
    return True


@func_speed
def second(x):
    return x % sum(list(map(int, str(x)))) == 0


@func_speed
def genius(x):
    return x % sum(int(x) for x in str(x)) == 0


first(9892)
second(9892)
genius(9892)
