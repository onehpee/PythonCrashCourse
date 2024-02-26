# Names
# Make a list of names
# Print individual elements of the list
names = ['Boyee', 'Uyii', 'Oseratinn', 'Ifee']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# Greetings
# Print a message to each name
text_1 = f"Hi! My name is {names[0].title()}"
text_2 = f"Hi! My name is {names[1].title()}"
text_3 = f"Hi! My name is {names[2].title()}"
text_4 = f"Hi! My name is {names[3].title()}"
print(text_1)
print(text_2)
print(text_3)
print(text_4)

# Your own list
cars = ['mercedes benz', 'porche', 'ferrari', 'honda']
statement_1 = f"I would like to own a {cars[0].title()} car one day."
statement_2 = f"I would like to own a {cars[1].title()} car one day."
statement_3 = f"I would like to own a {cars[2].title()} car one day."
statement_4 = f"I would like to own a {cars[3].title()} car one day."
print(statement_1)
print(statement_2)
print(statement_3)
print(statement_4)

# Remove() Exercise 3-4 - 3-6

guess_list = ['beyonce', 'bruce lee', 'patrice oneal']

print(f"{guess_list[0].title()}, you have officially been invited to dinner!")
print(f"{guess_list[1].title()}, you have officially been invited to dinner!")
print(f"{guess_list[2].title()}, you have officially been invited to dinner!")

no_show = guess_list.pop(2)
print(f"{no_show}, unfortunately can not make it to the dinner")

guess_list.append('dave chappelle')
print(f"{guess_list[0].title()}, you have officially been invited to dinner!")
print(f"{guess_list[1].title()}, you have officially been invited to dinner!")
print(f"{guess_list[2].title()}, you have officially been invited to dinner!")

guess_list.insert(0, 'rihanna')
guess_list.insert(2, 'zendaya')
guess_list.append('tyla')

print('With great joy, we would like to annouce a bigger table has been found!')

print(f"{guess_list[0].title()}, you have officially been invited to dinner!")
print(f"{guess_list[1].title()}, you have officially been invited to dinner!")
print(f"{guess_list[2].title()}, you have officially been invited to dinner!")
print(f"{guess_list[3].title()}, you have officially been invited to dinner!")
print(f"{guess_list[4].title()}, you have officially been invited to dinner!")
print(f"{guess_list[5].title()}, you have officially been invited to dinner!")

print('We are sad to annouce, that the dinner table will not arrive in time')

no_space = guess_list.pop()
print(f"{no_show}, unfortunately we no longer have space for you at the table")
no_space = guess_list.pop()
print(f"{no_show}, unfortunately we no longer have space for you at the table")
no_space = guess_list.pop()
print(f"{no_show}, unfortunately we no longer have space for you at the table")
no_space = guess_list.pop()
print(f"{no_show}, unfortunately we no longer have space for you at the table")


