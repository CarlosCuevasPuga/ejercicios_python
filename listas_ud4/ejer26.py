nums = []

while True:
    n = int(input("Introduce un número: "))
    if nums.count(n) == 0:
        nums.append(n)
    print(nums)
