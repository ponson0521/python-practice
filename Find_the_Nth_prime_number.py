# Find the Nth prime number

def get_prime(n):
    a = [2]
    num = 3
    while len(a) < n:
        for p in a:
            if num % p == 0:
                break
        else:
            a.append(num)
        num += 1
    return print(a[-1])


n = int(input('請輸入欲找出第幾個質數：'))
get_prime(n)
