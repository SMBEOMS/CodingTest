word = input()
croatia_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for ca in croatia_alphabets:
    word = word.replace(ca, '*')

print(len(word))
