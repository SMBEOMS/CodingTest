a = int(input())
results = []  # 결과를 저장할 리스트

for _ in range(a):
    coin = int(input())

    Quarter = coin // 25
    Quarter2 = coin % 25
    Dime = Quarter2 // 10
    Dime2 = Quarter2 % 10
    Nickel = Dime2 // 5
    Nickel2 = Dime2 % 5
    Penny = Nickel2 // 1

    results.append((Quarter, Dime, Nickel, Penny))

# 모든 입력에 대한 결과를 한 번에 출력
for result in results:
    print(*result)
