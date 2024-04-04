from mart import pi,sin,cos

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))

num1 = min(a,b,c,d)
num4 = max(a,b,c,d)

def second_max():
    if a == num4:
        if b>=c and b>=d:
            return b
        if c>=b and c>=d:
            return c
        if d>=b and d>=c:
            return d
    if b == num4:
        if a>=c and a>=d:
            return a
        if c>=a and c>=d:
            return c
        if d>=a and d>=c:
            return d
    if c == num4:
        if a>=b and a>=d:
            return a
        if b>=a and b>=d:
            return b
        if d>=a and d>=b:
            return d
    if d == num4:
        if a>=b and a>=c:
            return a
        if b>=a and b>=c:
            return b
        if c>=a and c>=b:
            return c
num3 = second_max()

def second_min():
    if a == num1:
        if b<=c and b<=d:
            return b
        if c<=b and c<=d:
            return c
        if d<=c and d<=b:
            return d
    if b == num1:
        if a<=c and a<=d:
            return a
        if c<=a and c<=d:
            return c
        if d<=c and d<=a:
            return d
    if c == num1:
        if b<=a and b<=d:
            return b
        if a<=b and a<=d:
            return a
        if d<=a and d<=b:
            return d
    if d == num1:
        if b<=c and b<=a:
            return b
        if c<=b and c<=a:
            return c
        if a<=b and a<=c:
            return a
num2 = second_min()

# N = (4+1)/2 = 2.5
# Med = ตัวหน้า + [(ตัวหลัง-ตัวหน้า)*ทศนิยม]

med = num2+((num3-num2)*0.5)
print(f"Median is {med:.2f}")