# 소수를 판별하는 함수 정의
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 입력 받기
M = int(input())
N = int(input())

# 소수인 수들을 저장할 리스트 초기화
prime_numbers = []

# M부터 N까지의 범위에서 소수를 찾아서 리스트에 추가
for num in range(M, N + 1):
    if is_prime(num):
        prime_numbers.append(num)

# 소수가 없을 경우 -1 출력, 아닌 경우 합과 최솟값 출력
if not prime_numbers:
    print(-1)
else:
    print(sum(prime_numbers))
    print(min(prime_numbers))
