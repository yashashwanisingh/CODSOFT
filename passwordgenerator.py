import random
letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','+']
print("!!!!WELCOME TO PASSWORD GENERATOR!!!!")
a=int(input("How many letters do you want in your password?: "))
b=int(input("How many numbers do you want in your password?: "))
c=int(input("How many symbols do you  want in your password?: "))
password=""
for i in range(1,a+1):#1,2,3,4
    char = random.choice(letters)
    password = password+char
for i in range(1,b+1):
    char = random.choice(numbers)
    password = password+char
for i in range(1,c+1):
    char = random.choice(symbols)
    password = password+char
print(password)
