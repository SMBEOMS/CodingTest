# 입력 받을 숫자의 개수 입력
n = int(input())

# 숫자로 이루어진 문자열 입력
numbers = input()

# 입력받은 숫자들을 모두 더하기
total = 0
for digit in numbers:
    total += int(digit)

# 결과 출력
print(total)
