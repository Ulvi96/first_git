# Temperature converter

unit = str(input("Is this temperature in Celsius or Fahrenheit (C or F): ")).strip().upper()
temperature = float(input("Enter the temperature: "))

if unit == "C":
    converted_temperature = (9 * temperature) / 5 + 32
    print(f"The temperature in Fahrenheit is: {converted_temperature:.2f}°F")
elif unit == "F":
    converted_temperature = (temperature - 32) * 5 / 9
    print(f"The temperature in Celsius is: {converted_temperature:.2f}°C")
else:
    print(f"{unit} is an invalid unit of measurement")