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

# Reverse() doesn't sort backward alphabetically; it simply reverse the order of the list
# The reverse() method changes the order of a list permanently, you can revert it back by using revers() the same list

# Finding the Length of a list
# You can quickly find the length of a list by using the len() function.

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

# Seeing the world

vacation_spots = ['japan', 'brazil', 'new york', 'dominican republic', 'miami']
print(vacation_spots)

print(sorted(vacation_spots))

print(vacation_spots)

vacation_spots.reverse()
print(vacation_spots)

vacation_spots.reverse()
print(vacation_spots)

vacation_spots.sort()
print(vacation_spots)

vacation_spots.sort(reverse=True)
print(vacation_spots)

# Dinner Guests
guess_list = ['beyonce', 'bruce lee', 'patrice oneal']
print(f'There are {len(guess_list)}, number of people invited to dinner')