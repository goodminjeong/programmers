def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    answer1 = ((x1 - x2) / (x3 - x4)) == ((y1 - y2) / (y3 - y4))
    answer2 = ((x1 - x3) / (x2 - x4)) == ((y1 - y3) / (y2 - y4))
    answer3 = ((x1 - x4) / (x2 - x3)) == ((y1 - y4) / (y2 - y3))
    return 1 if answer1 or answer2 or answer3 else 0


print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))
print(solution([[1, 0], [0, 1], [1, 2], [2, 1]]))
print(solution([[1, 1], [4, 2], [5, 5], [7, 7]]))
