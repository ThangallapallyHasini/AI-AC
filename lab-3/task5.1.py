def temp_converter():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius") 
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    
    choice = input("Enter choice (1-4): ")
    temp = float(input("Enter temperature: "))
    
    if choice == "1":
        result = (temp * 9/5) + 32
        print(f"{temp}°C = {result}°F")
    elif choice == "2":
        result = (temp - 32) * 5/9
        print(f"{temp}°F = {result}°C")
    elif choice == "3":
        result = temp + 273.15
        print(f"{temp}°C = {result}K")
    elif choice == "4":
        result = temp - 273.15
        print(f"{temp}K = {result}°C")
    else:
        print("Invalid choice!")

# Run the converter
temp_converter()