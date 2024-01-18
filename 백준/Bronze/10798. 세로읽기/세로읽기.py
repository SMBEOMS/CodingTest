# 5개의 문자열 입력받기
strings = [input() for _ in range(5)]

# 최대 길이 구하기
max_length = max(len(s) for s in strings)

# 세로로 읽기
result = ''
for i in range(max_length):
    for string in strings:
        if i < len(string):
            result += string[i]

# 결과 출력
print(result)
