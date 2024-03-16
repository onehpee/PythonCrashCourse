# Slicing a List
players = ['ade', 'boye', 'princess', 'uyi', 'oso']
print(players[0:3])
# The output retains the structure of the list and includes the firt three players in the list

# You can generate any subset of a list. Like second, third, and fourth item in a list
print(players[1:4])

# if you omit the first index in a slice, Python automatically starts your slice at the beginning of the list
print(players[:4])

# Python returns all items from the third item through the end of the list
print(players[2:])

# This prints the names of the last three players and would continue to work as the list of players change  in size
print(players[-3:])


# Looping Through a Slice
players = ['ade', 'boye', 'princess', 'uyi', 'oso']

print('Here are the first three players on my team: ')
for player in players[:3]:
    print(player.title())