nums = []

while True:
    num = int(input("Inserta un número: "))
    if num == 0:
        break
    nums.append(num)


print(f"El maximo es {max(nums)}")
print(f"El minimo es {min(nums)}")
print(f"La media es {sum(nums) / len(nums)}")