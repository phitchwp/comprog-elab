weight = float(input("Input weight (kg): "))
height = float(input("Input height (m): "))
bmi = weight/(height)**2
print(f"Your BMI now is {bmi:.1f}")
bmi22 = 22*(height)**2
print(f"Your weight for BMI=22 is {bmi22:.1f} kg.")