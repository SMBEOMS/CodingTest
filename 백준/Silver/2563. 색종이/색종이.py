# 도화지를 나타내는 2차원 배열 초기화 (100x100, 초기값은 0)
paper = [[0] * 100 for _ in range(100)]

# 색종이의 수 입력 받기
n = int(input())

for _ in range(n):
    # 색종이의 왼쪽 하단 꼭짓점 좌표 입력 받기
    x, y = map(int, input().split())

    # 해당 위치에 색종이를 붙임 (색종이 면적만큼 1로 채움)
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

# 면적 계산
area = sum(sum(row) for row in paper)

# 결과 출력
print(area)