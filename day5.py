import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
no_letters = int(input("How many letters would you like in your password? \n"))
no_symbols = int(input("How many symbols would you like in your password? \n"))
nums = int(input("How many numbers would you like in your password? \n"))

password = ''

choices = random.choices(letters, k=no_letters)
for choice in choices:
    password += choice
symbols_1 = random.choices(symbols, k= no_symbols)
for symbol in symbols_1:
    password += symbol
num_1 = random.choices(numbers, k= nums)
for number in num_1:
    password += number

# For the random.shuffle to work password must be a list
l = list(password)
randomize = random.shuffle(l)
# The join method concatenates each character in the list l into a single string. 
# The separator between characters is an empty string (''), meaning they are joined without any space 
# or character in between.
result = ''.join(l)  
print("Password is: ", result)