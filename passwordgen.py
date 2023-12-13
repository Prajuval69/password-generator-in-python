import random
import string
letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
symbols = list(string.punctuation)
numbers = [str(i) for i in range(10)]
letter=int(input("enter the number of letters required in the password: "))
symbol=int(input("enter the number of symbols required in the password: "))
number=int(input("enter the number of numbers required in the password: "))
password=""
for i in range(1,letter+1):
    l=random.choice(letters)
    password+=l
    
for i in range(1,symbol+1):
    s=random.choice(symbols)
    password+=s

for i in range(1,number+1):
    n=random.choice(numbers)
    password+=n

temp=list(password)
random.shuffle(temp)
npassword=''.join(temp)
print('The required password is :')
print(npassword)
