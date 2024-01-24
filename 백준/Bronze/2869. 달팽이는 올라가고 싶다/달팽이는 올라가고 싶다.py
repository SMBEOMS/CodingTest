import math

A, B, V = map(int, input().split())

# 정상에 도달하는데 필요한 일수 계산
# 낮에 정상에 도달하면 미끄러지지 않으므로 V-B를 계산
days = (V - B) / (A - B)

# 올라가는데 필요한 일수는 정수여야 하므로 올림 처리
days = math.ceil(days)

print(days)