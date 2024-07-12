import sys
input = sys.stdin.readline


n1 = int(input().strip())
num1 = list(map(int, input().strip().split()))


n2 = int(input().strip())
num2 = list(map(int, input().strip().split()))

_dict = {}
for num in num1:
    if num in _dict:
        _dict[num] += 1
    else:
        _dict[num] = 1

result = []
for num in num2:
    if num in _dict:
        result.append(_dict[num])
    else:
        result.append(0)

print(' '.join(map(str, result)))
