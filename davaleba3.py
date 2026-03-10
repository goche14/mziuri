#1
#a=15
#b=4

#print(a + b)
#print(a - b)
#print(a * b)
#print(a / b)
#print(a // b)
#print(a**b)

#2

#first_name = "ana"
#last_name = " gelashvili"
#full_name = first_name + last_name
#print(full_name)

#3

#number1 = "25"
#number2 = "30"
#print(number1+number2)
#print(int(number1)+int(number2))

#4
#name = input("enter your name: ")
#age = int(input("enter your age: "))
#fav_country = input("enter your favorite country: ")

#print(f"gamarjoba {name} shen xar {age} wlis da sheni sayvareli qveyanaa {fav_country}")

#5

num1 = int(input("enter num: "))
num2 = int(input("enter num: "))

opperation = input("1.+ , 2.-, 3.*, 4./, enter opperation number: ")

if opperation == "1":
    print(num1+num2)
elif opperation == "2":
    print(num1-num2)
elif opperation == "3":
    print(num1*num2)
else:
    print(num1/num2)
