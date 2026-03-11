n = int(input("enter num: "))
count_luwi = 0
count_kenti = 0

for i in range(1,n+1):
    if i % 2 == 0:
        count_luwi += 1
    else:
        count_kenti += 1

print(f"kentebi {count_kenti}")
print(f"luwebi {count_luwi}")
        