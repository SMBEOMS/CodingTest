N, B = map(int, input().split())
result = ''

# N을 B진법으로 변환
while N > 0:
    remainder = N % B
    # 10 이상의 수를 알파벳으로 변환
    if remainder >= 10:
        result += chr(remainder + 55)  # 'A'는 65, 'B'는 66, ...
    else:
        result += str(remainder)
    N //= B

# 결과를 역순으로 출력 (최상위 자리부터 출력해야 하므로)
print(result[::-1])
