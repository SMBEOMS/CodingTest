a = int(input())
old_name = []
for _ in range(a):
    old, name = input().split()
    old = int(old)
    old_name.append((old, name))
    
old_name.sort(key = lambda x : x[0])	

for i in old_name:
    print(i[0],i[1])