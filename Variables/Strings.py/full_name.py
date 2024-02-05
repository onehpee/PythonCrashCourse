first_name = "adedayo"
last_name = "uwensuyi"
#f-strings, F stands for format
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)

#python 3.5 version of format stings
full_name2 = "{} {}".format(first_name, last_name)