def solution(my_string):
    answer = []
    set_string = set(list(my_string))
    for i in list(my_string):
        if i in set_string:
            if not i in answer:
                answer.append(i)
    return ''.join(answer)

print(solution("people"))
print(solution("We are the world"))