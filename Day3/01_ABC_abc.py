def solution(my_string):
    answer = ''
    for string in my_string:
        if string.isupper():
            answer = string.lower()
        else:
            answer = string.upper()
    return answer

print(solution("CCCccc"))
print(solution("abCdEfghIJ"))

# 출력화면
# cccCCC
# ABcDeFGHij