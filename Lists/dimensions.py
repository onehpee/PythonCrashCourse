# Dimensions of rectangle
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# This won't work and will throw an error because you can't alter a tuple
# dimensions[0] = 250

# A tuple with one element is typically used but it goes like this
# my_t = (3,)


# Looping over all values in a tuple
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
    
    
# Writing over a tuple
# Although you can't modify a tuple, you can assign a new value to a variable that represents a tuple
# So if we wanted to change our dimensions, we could redefine the entire tuple
dimensions = (200, 50)
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)
    
