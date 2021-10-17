s = input("Surname: ")
n = input("Name: ")
y = input("Year: ")
c = input("City: ")
e = input("E-mail: ")
p = input("Phone: ")

def user_info(surname, name, year, city, email, phone):
    print(f'{surname} {name} {year} {city} {email} {phone}')

user_info(surname=s, name=n, year=y, city=c, email=e, phone=p)