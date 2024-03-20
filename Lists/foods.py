# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print('My favorite foods are: ')
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

# We make a copy of my_foods by asking for a slice of my_foods without specifying any indices
# And store the copy in friends_foods. When we print each list, we see that they both contain the same foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

# Try it yourself
print('The first three items in the list are: ')
print(my_foods[0:2])

print('The three items from the middle of the list are: ')
print(my_foods[1:3])

print('The last three items of the list are: ')
print(my_foods[-3:])

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_pizzas = my_foods[:]
my_foods.append('mushroom')
friend_pizzas.append('fish')

