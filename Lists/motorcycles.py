# Modifying Elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Apending Elements in a list
# New elements are added to the end of the list by using the append() method
motorcycles.append('ducati')
print(motorcycles)

fruit = []

fruit.append('apple')
fruit.append('grape')
fruit.append('coconut')

print(fruit)

# Inserting into a list
# YOu can add a new elements at any position in your list by using the insert() method

colors = ['black', 'brown', 'white']
colors.insert(0, 'yellow')
print(colors)

# Removing Elements from a list
# You can remove any item according to its position in the list or according

insects = ['spiders', 'flies', 'ladybugs']
print(insects)

del insects[0]
print(insects)

# Sometimes you''ll want to use the value of an item after you remove it from a list
# The pop() removes that last itme in a list
# Top of a stack corresponds to the end of a list

insects = ['spiders', 'flies', 'ladybugs']
print(insects)

popped_insects = insects.pop()
print(insects)
print(popped_insects)

insects = ['spiders', 'flies', 'ladybugs']
last_insect = insects.pop()
print(f"The last insect i saw was a {last_insect.title()}.")


# Popping Elements from any position
# You can do that putting the index of the element in the parentheses

insects = ['spiders', 'flies', 'ladybugs']

first_insect = insects.pop(0)
print(f"The first insect I saw was a {first_insect.title()}.")


# Sometimes you won't know the position of the value you want to remove frome a list
# If you only know the value of the item you want to remove, you can use remove() method

insects = ['spiders', 'flies', 'ladybugs']
print(insects)

insects.remove('ladybugs')
print(insects)

# Working with the value removed from the list
insects = ['spiders', 'flies', 'ladybugss']
print(insects)

too_ugly = 'spiders'
insects.remove(too_ugly)
print(insects)
print(f"\nA {too_ugly.title()} is too ugly for me")