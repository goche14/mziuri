n = int(input("enter num: "))
i = int(input("enter larger num: "))

jami = 0

for x in range(n,i+1):
    if x % 2 == 0:
        jami += 1


print(jami)
