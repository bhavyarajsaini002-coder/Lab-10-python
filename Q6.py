def get_grade(marks):
    if marks >= 80:
        return 'A'
    elif marks >= 60:
        return 'B'
    elif marks >= 40:
        return 'C'
    else:
        return 'F'

n = int(input("Enter N: "))
grade_counts = {}
grade_order = []
students_data = []

for _ in range(n):
    line = input().split()
    name = line[0]
    marks = int(line[1])
    g = get_grade(marks)
    students_data.append((name, g))
    
    if g not in grade_counts:
        grade_counts[g] = 1
        grade_order.append(g)
    else:
        grade_counts[g] += 1

for name, g in students_data:
    print(name + ": " + g)

print("Grade count:")
ordered_counts = {}
for g in grade_order:
    ordered_counts[g] = grade_counts[g]

print(ordered_counts)