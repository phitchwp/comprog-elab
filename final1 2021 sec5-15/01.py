# โจทย์ให้เรา input ค่า n (ตัวเลข)
# output ออกมาเป็นจำนวนของจำนวนเฉพาะนั้นจนถึง n

def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

n = int(input("Please enter the n value: "))
if n > 0:
    cPrime = 0
    for i in range(1,n):
        if isPrime(i):
            cPrime += 1
    print(f"The total number of prime number is {cPrime}")
else:
    print("!!! Error occured, use positive number only!")