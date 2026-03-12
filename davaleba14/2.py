numbers = [1,2,4,5,6,2,8,4,10]
even_numbers = []

for num in numbers:
    if num % 2 == 0:          
        if num not in even_numbers:
            even_numbers.append(num)

print(even_numbers)