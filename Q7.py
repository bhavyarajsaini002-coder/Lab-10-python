tup = tuple(int(x) for x in input("Enter numbers: ").split())
even_list = []

for x in tup:
    if x % 2 == 0:
        even_list.append(x)

even_tup = tuple(even_list)
print(even_tup)