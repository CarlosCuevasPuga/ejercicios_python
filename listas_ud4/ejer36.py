nums = []

while True:
    num = int(input("Inserta un número: "))
    if num == 0:
        break
    nums.append(num)

n_ultimos = int(input("Cuantos números quieres mostrar? "))
nums.reverse()
print(f"Los últimos {n_ultimos} números son:")
for i in range(n_ultimos):
    print(nums[i])
    i += 1