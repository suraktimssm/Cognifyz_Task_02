temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C/F): ").strip().upper()

if unit == "C":
    converted = (temp * 9/5) + 32
    print(f"Temperature in Fahrenheit: {converted}°F")
elif unit == "F":
    converted = (temp - 32) * 5/9
    print(f"Temperature in Celsius: {converted}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")