# Solution to Exercise 2: Ticket Pricing
age = int(input("Enter the visitor's age: "))

if 0 <= age <= 2:
    ticket_price = 0
elif 3 <= age <= 12:
    ticket_price = 10
elif 13 <= age <= 65:
    ticket_price = 20
else:
    ticket_price = 15

print(f"The ticket price is: ${ticket_price}")
