nums = []

while True:
    num = int(input("Inserta un número: "))
    if num == 0:
        break
    nums.append(num)

nums.sort()
print(nums)