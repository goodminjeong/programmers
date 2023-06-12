def solution(my_string):
    answer = ''
    for st in my_string:
        answer += st.lower()
    list_answer = sorted(list(answer))
    return ''.join(list_answer)


print(solution("Bcad"))
print(solution("heLLo"))
print(solution("Python"))

# 출력화면
# bcad
# hello
# python
