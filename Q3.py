votes = input("Enter votes: ").split()
vote_dict = {}
order = []

for name in votes:
    if name not in vote_dict:
        vote_dict[name] = 1
        order.append(name)
    else:
        vote_dict[name] += 1

max_votes = -1
winner = ""

for name in order:
    print(name + ":", vote_dict[name])
    if vote_dict[name] > max_votes:
        max_votes = vote_dict[name]
        winner = name

print("Winner:", winner)