nums_list = [int(x) for x in input("Enter integers: ").split()]
V = int(input("Enter value V: "))

# Convert list to tuple
tup = tuple(nums_list)

print("Tuple:", tup)
print("Length:", len(tup))
print("Count of", V, ":", tup.count(V))
print("First index of", V, ":", tup.index(V))