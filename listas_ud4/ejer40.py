nums = input("Inserta números separados por punto y coma: ").split(";")

for i in range(len(nums)):
    nums[i] = int(nums[i])

print(f"El número mayor es: {max(nums)}")
print(f"El número menor es: {min(nums)}")
print(f"La suma es: {sum(nums)}")
print(f"El número mayor es: {sum(nums) / len(nums)}")