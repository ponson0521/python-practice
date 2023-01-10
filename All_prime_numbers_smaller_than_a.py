# All prime numbers < a
a = int(input('請輸入一個正整數:'))
b = []

for i in range(1, a+1):
    c = 0
    for j in range(1, i+1):
        if i % j == 0:
            c += 1
    if c == 2:
        b.append(i)

print('小於', a, '的質數為:', b)
