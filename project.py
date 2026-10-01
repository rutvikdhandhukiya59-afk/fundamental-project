
print("=" * 50)
print("WELCOME TO THE PERSONAL DATA COLLECTOR")
print("=" * 50)



name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
fav_number = int(input("Enter your favourite number: "))

print("\nData collected successfully!")


current_year = 2026
birth_year = current_year - age



height_int = int(height)


print("\n" + "=" * 50)
print("VARIABLE INFORMATION")
print("=" * 50)

print(f"Name = {name}")
print("Type:", type(name))
print("Memory Address:", id(name))

print("\nAge =", age)
print("Type:", type(age))
print("Memory Address:", id(age))

print("\nHeight =", height)
print("Type:", type(height))
print("Memory Address:", id(height))

print("\nFavourite Number =", fav_number)
print("Type:", type(fav_number))
print("Memory Address:", id(fav_number))



sum_value = age + fav_number
difference = age - fav_number
multiplication = age * fav_number
division = age / fav_number

print("\n" + "=" * 50)
print("ARITHMETIC OPERATIONS")
print("=" * 50)

print("Age + Favourite Number =", sum_value)
print("Age - Favourite Number =", difference)
print("Age * Favourite Number =", multiplication)
print("Age / Favourite Number =", division)


print("\n" + "=" * 50)
print("TYPE CASTING")
print("=" * 50)

print("Original Height:", height, "Type:", type(height))
print("Height converted to Integer:", height_int)
print("Type after conversion:", type(height_int))


print("\n" + "=" * 50)
print("PERSONAL DATA SUMMARY")
print("=" * 50)

print(f"Name            : {name}")
print(f"Age             : {age}")
print(f"Height          : {height} meters")
print(f"Favourite Number: {fav_number}")
print(f"Birth Year      : {birth_year}")

print("\nThank you for using the Personal Data Collector!")
print("Keep learning Python. Goodbye!")