n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(input())

row = 0
column = 0

for i in range(n):  # 행 반복
    if "X" not in board[i]:
        row += 1

for j in range(m):  # 열 반복
    c = False
    for i in range(n):  # 열별로 행을 검사
        if board[i][j] == "X":
            has_guard = True
            break
    if c == True:
        column += 1

result = max(row, column)
print(result)