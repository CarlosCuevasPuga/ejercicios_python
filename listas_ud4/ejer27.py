import random

nums = []
num_mas_repetido = 0

for _ in range(1, 1001):
    num_aleatorio = random.randint(1, 100)
    nums.append(num_aleatorio)

for cada_num in nums:
    if num_mas_repetido < nums.count(cada_num):
        num_mas_repetido = cada_num

print(f"El num mas repetido es {num_mas_repetido} y se repite {nums.count(num_mas_repetido)}")