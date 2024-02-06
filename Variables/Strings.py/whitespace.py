# in programming, whitespace refers to any nonprinting character, such as spaces, tabs, and end-on-line sybols
# You use white spaces to organize your output and make it more readable

# To add a Tab in a string you use \t
print("Python")
print("\tPython")

# To add a New Line in a string you use \n
print("Language:\nPython\nC\nJavaScript")

# You can also combine them 
print("Language:\n\tPython\n\tC\n\tJavaScript")

# Stripping Whitespace
# Extra whitespace can confuse a program, especially when comparing strings

favorite_language = "'python '"
print(favorite_language)
#This is only a temporary change
print(favorite_language.rstrip())
# This is the right way to do it, you have to reassign a valuable.
# This is how a variable's value can be updated as program is executed or in response to user input
favorite_language = favorite_language.rstrip()
print(favorite_language)