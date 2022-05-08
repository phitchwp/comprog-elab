week = input("Is a weekday?(y/n): ")
va = input("Is a vacation?(y/n): ")
if week == "y" and va == "y":
    print("You can sleep.")
elif week == "n" and va == "n":
    print("You can sleep.")
elif week == "y" and va == "n":
    print("You cannot sleep.")
elif week == "n" and va == "y":
    print("You can sleep.")
else:
    print("You cannot sleep.")
