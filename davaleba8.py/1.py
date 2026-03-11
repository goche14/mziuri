for i in range(1,11):
    for x in range(1,11):
        namravli = i * x
        if namravli % 2 ==0:
            print(namravli, end="\t")