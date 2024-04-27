# Testing Multiple Conditions
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza")

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")


requested_toppings_toos = []

if requested_toppings_toos:
    for requested_toppings_too in requested_toppings_toos:
        print(f"Adding {requested_toppings_too}.")
    print("\Finished making your pizza!") 
else:
    print("Are you sure you want a plain pizza?")