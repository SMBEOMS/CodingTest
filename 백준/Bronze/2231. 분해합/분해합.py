a = int(input())

# 생성자를 찾는 과정
for i in range(1, a+1):
    # 분해합 계산
    original_number = i
    digits_sum = 0
    
    while original_number > 0:
        digits_sum += original_number % 10  # 오른쪽 자리수 더하기
        original_number //= 10  # 숫자를 10으로 나누어 다음 자리수 준비
    
    decomposed_sum = i + digits_sum
    
    # 분해합이 a와 같은 경우, i가 생성자
    if decomposed_sum == a:
        print(i)
        break
else:
    # 생성자가 없는 경우
    print(0)
