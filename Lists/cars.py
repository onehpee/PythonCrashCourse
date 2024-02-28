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

# Sorting a List Temporarily with the sorted() Function
# To maintain the orginal ordernof a list but present it in a sorted order, you can use the sorted()
# function. The sorted() funtion lets you display your list in a particular order but doesn't affect
# the actual order of the list.

print("Here is the orginal list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the orginal list again: ")
print(cars)


# Printing a List in Reverse Order
# To reverse the original order of a lisst, you can use the reverse() method.
print(cars)

cars.reverse()
print(cars)