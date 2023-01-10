# factorial_recursive

def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

a = int(input('請輸入整數:'))
print(factorial(a))
