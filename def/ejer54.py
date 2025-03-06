def factorial(num: int) -> int:
    fact = 1
    for i in range(1,num+1):
        fact = i * fact

    return fact

num = int(input("Introduce el número a factorizar: "))

print(factorial(num))

        