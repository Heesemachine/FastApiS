# players = ["Emily", "Alexander", "Sophia", "Benjamin", "Olivia", "William", "Ava", "James"]

# teams = []

# for i in range(len(players)):
#     for j in range(i + 1, len(players)):
#         team = (players[i], players[j])
#         teams.append(team)

# print(teams)

list1 = [1,2,3,4,5,6,7,8,9]

list2 = []

even = 0

for i in list1:
    if i % 2 == 0:
        list2.append(i)
print(list2)


thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)



thislist = [1,4,'Apple','Banana',1,4,5]

updatedlist = set(thislist)



print(updatedlist)

t ={i:i**2 for i in range(10) if i % 2 != 0}
print(t)