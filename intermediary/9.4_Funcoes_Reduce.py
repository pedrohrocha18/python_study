# Função reduce
# soma acumulativa
# reduce(função, sequência)

from functools import reduce


# def mult(x, y):
#     return x * y


# nums = [1, 2, 3, 4, 5, 7]

# total = reduce(mult, nums)

# print(total)


nums = [1, 2, 3, 4]

total = reduce(lambda x, y: x**2 + y**2, nums)

print(total)