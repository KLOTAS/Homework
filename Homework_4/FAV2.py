num_list = [360, 7, 12, 24, 2, 3, 5, 10, 7, 1, 56, 123, 99]
result = [num_list[i] for i in range(1, len(num_list)) if num_list[i] > num_list[i - 1]]
print(result)