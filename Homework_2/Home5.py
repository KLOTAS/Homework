rating_list = [9, 9, 5, 4, 3, 3, 3, 2, 1]

rating = int(input('Enter rating: '))
inserted = False
for index, elem in enumerate(rating_list):
    if rating > elem:
        rating_list.insert(index, rating)
        inserted = True
        break

if not inserted:
    rating_list.append(rating)

print(rating_list)
