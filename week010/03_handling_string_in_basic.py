"""
문자열 다루기 기본

<문제 설명>
- 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
- 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

<제한 조건>
- s는 길이 1 이상, 길이 8 이하인 문자열입니다.
- s는 영문 알파벳 대소문자 또는 0부터 9까지 숫자로 이루어져 있습니다.
"""
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from func_speed import func_speed


# 첫 번째 풀이
@func_speed
def solution1(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
        except:
            answer = False
    else:
        answer = False
    return answer


# 두 번째 풀이
@func_speed
def solution2(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False


solution1("a234")
solution2("a234")

solution1("1234")
solution2("1234")

solution1("51181234")
solution2("51181234")

solution1("123456")
solution2("123456")
