def solution(board):
    board_len = len(board)
        
    # 지뢰가 설치된 위치 찾기
    bomb = []
    for x in range(board_len):
        for y in range(board_len):
            if board[x][y] == 1:
                bomb.append((x, y))
                
    # 지뢰 주변을 1로 만들기
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for x, y in bomb:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < board_len and 0 <= ny < board_len:
                board[nx][ny] = 1
                
    # 0인 부분만 카운팅 하기
    count = 0
    for x in range(board_len):
        for y in range(board_len):
            if board[x][y] == 0:
                count += 1
    return count


print(solution([[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0]]))  # 16
print(solution([[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0]]))  # 13
print(solution([[1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1]]))   # 0
