a = list(map(int, input().split()))

chess = [1, 1, 2, 2, 2, 8]
make = [chess[i] - a[i] for i in range(6)]

print(" ".join(map(str, make)))