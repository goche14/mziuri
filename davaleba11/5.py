numbers = [1,2,3,4,5,6,7,8,9,10]

range = sum(numbers) / len(numbers)

for i in numbers:
    if i > range:
        print(i)