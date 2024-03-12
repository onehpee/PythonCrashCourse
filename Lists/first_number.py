# The range() function causes Python to start counting at the first value you give it, and it stops when it
# reaches the second value you provide. Because it stops at that second value, the output never contains the end 
# value, which would have been 5 in this case

for value in range(1, 5):
    print(value)
    
for values in range(1, 6):
    print(values)
    
    
# If you want to make a list of numbers, you convert the results of range() directly into a list using the list()
# function. When you wrap list() around a call to the range() function, the output will be a list of numbers.

numbers = list(range(1, 6))
print(numbers)