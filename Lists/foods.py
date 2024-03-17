# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print('My favorite foods are: ')
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

# We make a copy of my_foods by asking for a slice of my_foods without specifying any indices
# And store the copy in friends_foods. When we print each list, we see that they both contain the same foods