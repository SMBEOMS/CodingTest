# 테스트 케이스 수 입력
t = int(input())

# 테스트 케이스마다 반복 횟수와 문자열 입력받아 처리
for _ in range(t):
    r, s = input().split()
    r = int(r)
    
    # 문자열을 한 글자씩 반복해서 출력
    for char in s:
        print(char * r, end='')

    # 테스트 케이스마다 한 줄씩 출력
    print()
