a, b, c, d, e, f = map(int, input().split())

# x와 y를 계산
x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

# x와 y 출력 (문제에서 x와 y는 정수라고 했으므로, 정수로 변환하여 출력)
print(int(x), int(y))
