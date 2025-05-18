temp = float(input("Enter the temperature: "))
unit = input("Is this temperature is Celsius or Fahrenheit ? (C/F): ").lower()


if unit == 'c':
    temp = round((temp * 9) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp} °F")
elif unit == 'f':
    temp = round((temp - 32) * 5/9, 1) 
    print(f"The temperature in Celsius is : {temp} °C")
else:
    print(f"{unit} is an invalid unit of measurement.")
        
        