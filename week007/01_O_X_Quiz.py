def solution(quiz):
    answer = []
    for q in quiz:
        cal = q.split("=")
        formula_result = eval(cal[0])
        if int(cal[1]) == formula_result:
            answer.append("O")
        else:
            answer.append("X")
    return answer


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
# ['X', 'O']
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))
# ['O', 'O', 'X', 'O']
