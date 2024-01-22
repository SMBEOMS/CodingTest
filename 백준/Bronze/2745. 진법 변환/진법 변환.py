# N진법 수와 진법 N 입력 받기
num, base = input().split()

# 10진법으로 변환
decimal = int(num, int(base))

# 결과 출력
print(decimal)
