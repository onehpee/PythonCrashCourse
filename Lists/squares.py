squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    
print(squares) 

squares_2 = []
for value in range(1, 11):
    squares_2.append(value**2)
    
print(squares_2)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares_3 = [value**2 for value in range(1, 11)]
print(squares_3)

# Exercise - Try it yourself

for value in range(1, 20):
    print(value)
    
one_million = [value for value in range(1, 1000001)]
print(one_million)

# Summing a Million
print(min(one_million))
print(max(one_million))
print(sum(one_million))

# Odd Numbers
odd_numbers = [value for value in range(1, 20, 2)]
print(odd_numbers)


# Threes
threes = [value * 3 for value in range(3, 30)]
print(threes)