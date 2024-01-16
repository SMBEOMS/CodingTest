n, m = map(int, input().split())

# 두 행렬을 저장할 리스트 초기화
matrix_a = [list(map(int, input().split())) for _ in range(n)]
matrix_b = [list(map(int, input().split())) for _ in range(n)]

# 두 행렬을 더하는 과정
result = [[matrix_a[i][j] + matrix_b[i][j] for j in range(m)] for i in range(n)]

# 결과 출력
for row in result:
    print(*row)
