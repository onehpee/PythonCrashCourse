# Try it Yourself
# 5.2 More Conditional Tests

string = 'laces'

if string == 'laces':
    print("Equality")
    
if string != 'shoes':
    print('Inequality')
    print("Hold the laces!")
    
case = 'BANG'

if case == 'BANG':
    print("True! BANG!")
    
if case.lower() == 'BANG':
    print("False! Dud!")
    
if 1 > 2:
    print("One not greater than two.")
    
if 1 < 2:
    print("One is less than two.")
    
if 2 >= 2:
    print("Two is greater than or equal to two.")
    
if 2 <= 2:
    print("Two is less than or equal to twoo.")
    
if 3 < 4 and 4 < 5:
    print("All things are true")
    
if 3 < 4 or 4 < 3:
    print("Some things are true")
    
candy = ['reese', 'twix', 'snickers']
bars = 'kit kat'
peanutB = 'reese'

if peanutB in candy:
    print(f"{peanutB.title()}, is has has peanut butter in it")

if bars not in candy:
    print(f"{bars.title()}, this has multiple bars")