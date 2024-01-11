word = input().upper()

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

time = 0

for char in word:
    for idx, letters in enumerate(dial):
        if char in letters:
            time += (idx + 3)

print(time)
