def Fibo(n):
    if (n <= 1):
        return n
    else:
        return Fibo(n-1) + Fibo(n-2)
print(Fibo(9))