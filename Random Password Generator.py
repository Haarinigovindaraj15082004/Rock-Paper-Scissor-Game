import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@','#','$','%','&','*']

print("Welcome to Password Generator")
n_letters = int(input("How many letters would you like to generate? "))
n_numbers = int(input("How many numbers would you like to generate? "))
n_symbols = int(input("How many symbols would you like to generate? "))
password_list = []

for i in range(1, n_letters+1):
    password_list.append(random.choice(letters))
    password_list.append(random.choice(numbers))
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password="".join(password_list)
print(password)