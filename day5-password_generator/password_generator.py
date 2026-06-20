import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#
# random_letter = random.choice(letters)
# random_symbol = random.choice(symbols)
# random_number = random.choice(numbers)



password = ""
# for i in range(1, nr_letters + 1):
#     password += random.choice(letters)
#
# for i in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#
# for i in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
#
# print(password)
i = 1
j = 1
k = 1
n= 1
for n in range(1, nr_letters + nr_symbols + nr_numbers + 1):
    random_selector = random.randint(0, 2)
    if i > nr_letters:
        random_selector_new0 = [1, 2]
        random_selector = random.choice(random_selector_new0)
        if j > nr_symbols:
            random_selector = 2
        if k > nr_numbers:
            random_selector = 1

    if j > nr_symbols:
        random_selector_new1 = [0, 2]
        random_selector = random.choice(random_selector_new1)
        if i > nr_letters:
            random_selector = 2
        if k > nr_numbers:
            random_selector = 0

    if k >nr_numbers:
        random_selector_new2 = [0, 1]
        random_selector = random.choice(random_selector_new2)
        if i > nr_letters:
            random_selector = 1
        if j > nr_symbols:
            random_selector = 0


    if random_selector == 0 and i <= nr_letters:
        for i in range(1, nr_letters + 1):
            password += random.choice(letters)
            i += 1
            break

    elif random_selector == 1 and j <= nr_symbols:
        for j in range(1, nr_symbols + 1):
            password += random.choice(symbols)
            j += 1
            break

    elif random_selector == 2 and k <= nr_numbers:
        for k in range(1, nr_numbers + 1):
            password += random.choice(numbers)
            k += 1
            break

    n += 1

print(password)
print(i)
print(j)
print(k)
