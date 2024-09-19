print("Welcome to the tip calculator")


bill = float(input("What was the total of the bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people_number = int(input("How many people are splitting the bill?"))

paying = round(float((bill + (tip_percentage/100)*bill)/people_number),2)

print(f"Each person should pay: ${paying}")