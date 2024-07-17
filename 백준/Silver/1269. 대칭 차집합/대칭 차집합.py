n, m = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

sym_diff = len(a ^ b) 
print(sym_diff)
