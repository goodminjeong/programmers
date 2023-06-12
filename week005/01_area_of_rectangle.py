def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])


dots = [[0, -2], [0, 3], [3, -2], [3, 3]]

print(max(dots)[0])     # 3
print(min(dots)[0])     # 0
print(max(dots)[1])     # 3
print(min(dots)[1])     # -2
print(max(dots))        # [3, 3]
print(min(dots))        # [0, -2]
print(solution(dots))   # 15
