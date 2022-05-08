unit = int(input("Unit: "))
def find_cost(unit):
    if unit <=7:
        cost = 110
    elif unit <= 18:
        cost = 110+(18*(unit-7))
    elif unit <= 43:
        cost = 110+(18*11)+21.5*(unit-18)
    elif unit <= 80:
        cost = 110+(18*11)+(21.5*25)+25*(unit-43)
    elif unit > 80:
        cost = 110+(18*11)+(21.5*25)+(25*37)+(10.5*(unit-80))
    return cost
print(f"Cost: {find_cost(unit):.2f} baht") 
