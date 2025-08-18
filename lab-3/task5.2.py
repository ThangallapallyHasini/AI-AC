def temp_converter():
    print("=== Temperature Converter ===")
    print("Available conversions:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius") 
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Celsius to Réaumur")
    print("6. Réaumur to Celsius")
    
    choice = input("\nEnter your choice (1-6): ")
    
    try:
        temp = float(input("Enter temperature value: "))
        
        if choice == "1":
            result = (temp * 9/5) + 32
            print(f"\n{temp}°C = {result}°F")
        elif choice == "2":
            result = (temp - 32) * 5/9
            print(f"\n{temp}°F = {result}°C")
        elif choice == "3":
            result = temp + 273.15
            print(f"\n{temp}°C = {result}K")
        elif choice == "4":
            result = temp - 273.15
            print(f"\n{temp}K = {result}°C")
        elif choice == "5":
            result = temp * 4/5
            print(f"\n{temp}°C = {result}°Ré")
        elif choice == "6":
            result = temp * 5/4
            print(f"\n{temp}°Ré = {result}°C")
        else:
            print("Invalid choice! Please select 1-6.")
            
    except ValueError:
        print("Error: Please enter a valid number!")

# Run the converter
temp_converter()