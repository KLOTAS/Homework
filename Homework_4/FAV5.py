
from functools import reduce

num_list = [x for x in range(108, 1081) if x % 2 == 0]
print(reduce(lambda a, b: a * b, num_list))