# Sorting a List Permanently with the sort() Method

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# The sort method, shown at line 4, changes the order of the list permanently. The cars are
# now in alphabetical order, and we can never revert to ther original order

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# You can also sort this list in reverse alphabetical order by passing the arguement reverse=True
# to the sort() method. The following example sorts the list of cars in reverse alphabetical order
