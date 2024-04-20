import random
import string
#Greet user.
print("Welcome to the password generator!")
#Ask for length of passowrd.
length = int(input('\nEnter the length of password: '))
#Define data using string module.
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#Combine data & store data.
all = string.ascii_letters + string.digits + string.punctuation
#Making use of the random module to generate password.
password = "".join(random.sample(all,length))
#Print password.
print(password)


