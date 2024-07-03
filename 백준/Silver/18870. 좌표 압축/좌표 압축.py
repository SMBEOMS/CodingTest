import sys

input = sys.stdin.readline #반복문으로 여러줄 입력받는 상황에서 사용

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i] : i for i in range(len(arr2))}

for i in arr:
    print(dic[i], end = ' ')