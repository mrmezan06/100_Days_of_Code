
print("Welcome to the tipe calculator.")

bill = float(input("What was the total bill? $"))
person = int(input("How many people to split the bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

avg = (float)(bill / person)
tip = avg + (avg * (percentage/100.0))

print("Each person should pay: $%.1f" % tip)