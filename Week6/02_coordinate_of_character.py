def solution(keyinput, board):
    answer, limit = [0,0], []
    keys = {
        "up" : [0,1],
        "down" : [0,-1],
        "left" : [-1,0],
        "right" : [1,0]
    }

    limit.append(-(board[0] // 2))
    limit.append(board[0] // 2)

    limit.append(-(board[1] // 2))
    limit.append(board[1] // 2)

    for key in keyinput:
        answer[0] += keys[key][0]
        answer[1] += keys[key][1]
        if limit[0] > answer[0]:
            answer[0] = limit[0]
        if limit[1] < answer[0]:
            answer[0] = limit[1]
        if limit[2] > answer[1]:
            answer[1] = limit[2]
        if limit[3] < answer[1]:
            answer[1] = limit[3]

    return answer

print(solution(["left", "right", "up", "right", "right"],[11, 11])) # [2, 1]
print(solution(["down", "down", "down", "down", "down"],[7, 9]))    # [0, -4]
print(solution(["left", "left", "left", "right"],[3, 3]))           # [0, 0]