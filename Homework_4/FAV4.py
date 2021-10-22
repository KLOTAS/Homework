my_list = [1, 5, 5, 2, 9, 2, 7, 10, 8, 5]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)
