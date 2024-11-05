# Shopping card
from operator import truediv

foods = []
prices = []

while True:
    food = str(input("Enter a food to buy or type 'q' for quit: ")).strip()
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        try:
            price = float(input(f"Enter the price of a {food}: "))
            prices.append(price)
        except ValueError:
            print("Invalid price. Please enter a valid number.")

print("\n----- Your cart -----")
for food, price in zip(foods, prices):
    print(f"{food:<15}: ${price:^5.2f}")

print(f"\nTotal price is ${sum(prices):.2f}")


