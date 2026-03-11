students = ["გიორგი", "ნინო", "დავითი", "მარიამი", "ლუკა"]
grades = [85, 90, 78, 92, 88, 76, 95, 89]

print(len(students))
print(students[len(students)-1])
print(students[len(students)-2])
print(grades[2])
print(grades[-1])
grades[0] = 100
print(grades)
avg_first4 = sum(grades[:4]) / 4
print(avg_first4)
print(grades[2:])
print(len(grades))
print(max(grades))
print(min(grades))
print(sum(grades))