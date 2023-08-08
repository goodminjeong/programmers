"""
올바른 괄호

<문제 설명>
- 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다.
- 예를 들어
    "()()" 또는 "(())()" 는 올바른 괄호입니다.
    ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
- '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

<제한사항>
- 문자열 s의 길이 : 100,000 이하의 자연수
- 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
"""
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from func_speed import func_speed


@func_speed
def solution(s):
    sum_p = 0
    for p in s:
        if p == "(":
            sum_p += 1
        else:
            sum_p -= 1
        # for문이 돌다가 sum_p가 -1이 되면 false
        if sum_p == -1:
            break

    # for문이 다 돌고 sum_p가 0이면 true, 그 외 값은 false
    return sum_p == 0


solution("()()")
solution("(())()")
solution(")()(")
solution("(()(")
