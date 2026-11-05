n = int(input("Enter N: "))
capitals = {}

for _ in range(n):
    line = input().split()
    country = line[0]
    capital = line[1]
    capitals[country] = capital

search_country = input("Enter country to search: ")

if search_country in capitals:
    print(capitals[search_country])
else:
    print("Not found")