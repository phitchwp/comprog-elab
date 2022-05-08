from math import sqrt,sin
x = float(input("Please enter value of x: "))

if x <= 0:
    fx = 2*sqrt(-x) + 10
elif x <= 25:
    fx = (3*sin(x))**2
else:
    fx = 2*x**3 - 5
    
if x < 5:
    gx = 2*x + 3
else:
    gx = x**2 + (2*x) - 5

if gx <= 0:
    fgx = 2*sqrt(-gx) + 10
elif gx <= 25:
    fgx = (3*sin(gx))**2
else:
    fgx = 2*gx**3 - 5
    
print(f"f(x) is {fx:.3f}")
print(f"g(x) is {gx:.3f}")
print(f"f(g(x)) is {fgx:.3f}")
