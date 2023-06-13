import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from func_speed import func_speed


# 첫 번째 풀이
@func_speed
def solution1(phone_number):
    answer = ""
    for i in range(len(phone_number) - 4):
        answer += "*"
    answer += phone_number[-4:]
    return answer


# 두 번째 풀이
@func_speed
def solution2(phone_number):
    star = "".join(["*" for _ in range(len(phone_number) - 4)])
    answer = phone_number.replace(phone_number[:-4], star)
    return answer


# 세 번째 풀이
@func_speed
def solution3(phone_number):
    star = ""
    for _ in range(len(phone_number) - 4):
        star += "*"
    answer = phone_number.replace(phone_number[:-4], star)
    return answer


solution1("15898354856846665266")
solution2("15898354856846665266")
solution3("15898354856846665266")
