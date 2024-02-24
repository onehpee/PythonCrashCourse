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