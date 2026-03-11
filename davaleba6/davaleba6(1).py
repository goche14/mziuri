num1 = int(input("enter num: "))
num2 = int(input("enter num: "))
num3 = int(input("enter num: "))

while True:
    if num1 and num2 and num3 > 0:
        print(num1+num2+num3)
        break
    elif num1 and num2 > 0 and num3 < 0:
        print(num1+num2)
        break
    elif num1 and num3 > 0 and num2 < 0:
        print(num1+num3)
        break
    elif num3 and num2 > 0 and num1 < 0:
        print(num3+num2)
        break
    elif num1 or num2 or num3 == 0:
        if num1 and num2 > 0:
            print(num1+num2)
            break
        elif num3 and num2 > 0:
            print(num3+num2)
            break
        elif num3 and num1 > 0:
            print(num3+num1)
            break




