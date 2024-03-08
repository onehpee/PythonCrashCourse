# We define a for loop. This line tells Python to pull a name from the lists magicians, and associate it
# With the magicianssss
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    print(f"Thank you, everyone. That was a great magic show!")
    
    

pizza_types = ['pepporoni', 'sausage & mushroom', 'philly steak']
for pizza in pizza_types:
    print(f"I like {pizza.title()} pizza.")
    
print(f"I like {pizza_types[0]} pizza")
print(f"I like {pizza_types[1]} pizza")
print(f"I like {pizza_types[2]} pizza")

print("I really love pizza")

birds = ['harpy eagle', 'owl', 'crow']
for bird in birds:
    print(f"A {bird.title()} would make a great pet")
