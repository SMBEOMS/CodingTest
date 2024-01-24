results = []  # 결과를 저장할 리스트

while True:
    N = int(input())
    if N == -1:
        break

    # N의 약수 찾기 (자기 자신 제외)
    divisors = []
    for i in range(1, N):
        if N % i == 0:
            divisors.append(i)

    # 약수들의 합이 N과 같은지 확인
    if sum(divisors) == N:
        results.append(f"{N} = " + " + ".join(map(str, divisors)))
    else:
        results.append(f"{N} is NOT perfect.")

# 모든 입력에 대한 결과를 한 번에 출력
for result in results:
    print(result)
