# Calculator

operation = str(input("Enter the operation: "))
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if operation == "+":
    print(f"Result: {round(first_number + second_number, 2)}")
elif operation == "-":
    print(f"Result: {round(first_number - second_number, 2)}")
elif operation == "*":
    print(f"Result: {round(first_number * second_number, 2)}")
elif operation == "/":
    print(f"Result: {round(first_number / second_number, 2)}")
else:
    print(f"{operation} is not a valid operation.")