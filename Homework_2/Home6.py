products = []
counter = 1
command = ''
while command != "stop":
    name = input('Name: ')
    price = input('Price: ')
    amount = input('Amount: ')
    units = input('Units: ')
    products.append(
    (counter, {"Name": name, "Price": price, "Amount": amount, "Units": units})
    )
    counter += 1
    command = input("Write 'stop' for stop inputting: ")

result_list = {}
for numb, prod_dict in products:
    for key, value in prod_dict.items():
        if not result_list.get(key):
            result_list[key] = [value]
        else:
            result_list[key].append(value)

for key, value in result_list.items():
    result_list[key] = list(set(value))

print(result_list)



