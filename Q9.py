n = int(input("Enter N: "))
stock = {}
order = []

for _ in range(n):
    line = input().split()
    item = line[0]
    qty = int(line[1])
    stock[item] = qty
    order.append(item)

q = int(input("Enter Q transactions: "))

for _ in range(q):
    trans = input().split()
    action = trans[0]
    item = trans[1]
    qty = int(trans[2])
    
    if action == "SELL":
        if stock[item] < qty:
            print("Insufficient stock: " + item)
        else:
            stock[item] -= qty
    elif action == "ADD":
        if item in stock:
            stock[item] += qty
        else:
            stock[item] = qty
            order.append(item)

for item in order:
    print(item, stock[item])