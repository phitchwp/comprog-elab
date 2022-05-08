print("Temperature Conversion")
celcius = float(input("Enter celcius: "))
KELVIN = 273.15
F = (9/5)*celcius + 32
K = celcius + 273.15 
R = 4/5 * celcius
temp = input("Input type of temperature: ")
if temp == "K":
    print(f"{celcius:.2f} C = {K:.2f} K")
elif temp == "k":
    print(f"{celcius:.2f} C = {K:.2f} k")
elif temp == "F":
    print(f"{celcius:.2f} C = {F:.2f} F")
elif temp == "f":
    print(f"{celcius:.2f} C = {F:.2f} f")
elif temp == "R":
    print(f"{celcius:.2f} C = {R:.2f} R")
elif temp == "r":
    print(f"{celcius:.2f} C = {R:.2f} r")
else:
    print(f"There is no type {temp}.")