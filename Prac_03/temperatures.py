"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def celsius_function():
    global celsius
    celsius = float(input(5 / 9 * (fahrenheit - 32)))
    print("Result: {:.2f} C".format(celsius))


def fahrenheit_function():
    global fahrenheit
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit_function()
    elif choice == "F":
    
        celsius_function()
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

