import sys
cola = int(input("How many Cola?: "))
pokari = int(input("How many Pokari? "))
beer = int(input("How many Beer? "))
if cola < 0 or pokari < 0 or beer < 0:
    print("Invalid input. Program exits.")
    sys.exit()
    
total = cola*108 + pokari*250 + beer*800

print(f"The total cost is {total:.0f} yen.")

if total >= 0 and total <= 3000:
    discount = 0
elif total > 3000 and total <= 5000:
    discount = 500
elif total > 5000:
    discount = 1000
    
change = 10000-(total-discount)

print(f"The cost after discount is {total-discount} yen.")

if change < total-discount:
    print("Not enough money.")
elif change >= total-discount:
    print(f"Your change is {change} yen.")
    
if change >= 5000:
    print(f"5000-yen notes: 1")
    change = change - 5000
if change >= 1000:
    print(f"1000-yen notes: {change//1000}")
    change = change - (change//1000)*1000
if change >= 500:
    print(f" 500-yen coins: {change//500}")
    change = change - (change//500)*500
if change >= 100:
    print(f" 100-yen coins: {change//100}")
    change = change - (change//100)*100
if change >= 50:
    print(f"  50-yen coins: {change//50}")
    change = change - (change//50)*50
if change >= 10:
    print(f"  10-yen coins: {change//10}")
    change = change - (change//10)*10
if change >= 5:
    print(f"   5-yen coins: {change//5}")
    change = change - (change//5)*5
if change >= 1:
    print(f"   1-yen coins: {change}")

    