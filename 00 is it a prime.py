import sys
def isprime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    else:
        return True
while True:
    n = input("Enter an integer (or [Enter] to quit): ")
    if n == "":
        print("Bye!")
        sys.exit()
    n = int(n)
    if isprime(n):
        print(f"{n} is prime.")
    else:
        print(f"{n} is not prime.")
