user_input = input('List:')

input_list = user_input.split()

len_list = len(input_list)
i = 0
if len_list > 1:
    while i < len_list - 1:
        input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
        i += 2


print(input_list)