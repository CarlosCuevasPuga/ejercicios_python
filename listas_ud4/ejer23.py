nums = []

while True:
    n = int(input("Inserta un número: "))
    if n < 0:
        n_absoluto = abs(n)
        nums.remove(n_absoluto)
    else:
        nums.append(n)
    print(nums)