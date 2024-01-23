X = int(input())

# 현재 대각선의 최대 길이
diag_length = 1
# X가 속한 대각선을 찾기 위해 사용되는 누적 합
cumulative_sum = 1

# X가 속한 대각선 찾기
while X > cumulative_sum:
    diag_length += 1
    cumulative_sum += diag_length

# 대각선에서 X의 위치를 계산 (대각선 내에서의 상대적 위치)
position = X - (cumulative_sum - diag_length)

# 대각선의 번호에 따라 분모와 분자 계산
if diag_length % 2 == 0:
    numerator = position
    denominator = diag_length - position + 1
else:
    numerator = diag_length - position + 1
    denominator = position

print(f"{numerator}/{denominator}")
