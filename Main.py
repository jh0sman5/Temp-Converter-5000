# Temperature Converter - Input your temp and current unit - we'll convert it for you! 

## Global Variables

Celsius = "Celsius"
Fahrenheit = "Fahrenheit"
Kelvin = "Kelvin"

## Welcome Text

print("Hello there!")
print("Welcome to the Temperature Converter!")

while True:

    ## Obtain Inputs

    current_unit = input("What is your current temperature unit?\n(1) Celsius\n(2) Fahrenheit\n(3) Kelvin\nPlease enter Fahrenheit, Celsius, or Kelvin: \n")
    print("")
    current_temp = input("What is the current temperature?\nPlease enter a number: \n")
    print("")
    target_unit = input("What unit would you like to convert to?\n(1) Celsius\n(2) Fahrenheit\n(3) Kelvin\nPlease enter Fahrenheit, Celsius, or Kelvin: \n")
    print("")

    ## Calcuate Conversion

    if current_unit == "Celsius" and target_unit == "Fahrenheit": 
        new_temp = (float(current_temp) * 9/5) + 32
        print(f"{current_temp} in {current_unit} is {new_temp} in {target_unit}")
    elif current_unit == "Celsius" and target_unit == "Kelvin":
        new_temp = float(current_temp) + 273.15
        print(f"{current_temp} in {current_unit} is {new_temp} in {target_unit}")
    elif current_unit == "Fahrenheit" and target_unit == "Celsius":
        new_temp = (float(current_temp) - 32) * 5/9
        print(f"{current_temp} in {current_unit} is {new_temp} in {target_unit}")
    elif current_unit == "Fahrenheit" and target_unit == "Kelvin":
        new_temp = (float(current_temp) - 32) * 5/9 + 273.15
        print(f"{current_temp} in {current_unit} is {new_temp} in {target_unit}")
    elif current_unit == "Kelvin" and target_unit == "Celsius":
        new_temp = float(current_temp) - 273.15
        print(f"{current_temp} in {current_unit} is {new_temp} in {target_unit}")
    elif current_unit == "Kelvin" and target_unit == "Fahrenheit":
        new_temp = (float(current_temp) - 273.15) * 9/5 + 32
        print(f"{current_temp} in {current_unit} is {new_temp} in {target_unit}")
    else:
        print("Invalid input. Please ensure you entered the correct temperature units.")
    print("Thank you for using the Temperature Converter!")
    print("")
    again = input("Would you like to convert another temperature? (yes/no): \n").strip().lower()
    if again != "yes":
        break

## Goodbye Message

print("Goodbye!")
print("")
print("This program was created by Justin Hosman.")