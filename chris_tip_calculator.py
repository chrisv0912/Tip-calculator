#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
initial_bill=float(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give? 12,15, or 18? "))
people = int(input("How many people is the bill being split between? "))
bill_with_tip = (1+tip/100) * initial_bill
split_bill = bill_with_tip/people
rounded_bill = round(split_bill,2)
print(f"Bill split between {people} people will cost {rounded_bill} per person!")