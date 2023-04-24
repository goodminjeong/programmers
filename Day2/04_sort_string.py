def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
        else:
            pass
    sorted_answer = sorted(answer)
    return sorted_answer

print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))