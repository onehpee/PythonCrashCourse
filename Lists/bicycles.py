bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing individual elements in a list
print(bicycles[0])

# You can also use string methods on any element in this list.
print(bicycles[0].title())

# Index positions starts at 0, Not 1
print(bicycles[1])
print(bicycles[3])

# Pytohn has a special syntax fo accessing the last element in a list
# This is syntax is quite useful, because you'll often want to access
# the last items in a list without knowing exaclty how long the list is
# This convention extends to other negatice index valuses as well. 
# The index -2 returns the second to last item from the end of the list and so on and so forth.
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])