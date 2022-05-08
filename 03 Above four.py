

a = float(input("Please enter a: "))
b = float(input("Please enter b: "))
c = float(input("Please enter c: "))
d = float(input("Please enter d: "))
mean = (a+b+c+d)/4
numa,numb,numc,numd = 0,0,0,0
if a > mean:
    numa = 1
if b > mean:
    numb = 1
if c > mean:
    numc = 1
if d > mean:
    numd = 1
num =numa+numb+numc+numd
def num2():
    if num == 0:
        print("0 of these numbers is above average:")
        if num == 1:
            print("1 of these numbers is above average:")
        if num > 1:
            print(f"{num:.0f} of these numbers are above average:")
def aboveoffour():
    if a > mean:
        print(f"{a:.1f}")
    if b > mean:
        print(f"{b:.1f}")
    if c > mean:
        print(f"{c:.1f}")
    if d > mean:
        print(f"{d:.1f}")
num2()
aboveoffour()

