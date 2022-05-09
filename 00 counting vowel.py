string = input("Input a string: ")
counta,counte,counti,counto,countu = 0,0,0,0,0
for char in string:
  if char in "Aa":
    counta += 1
  if char in "Ee":
    counte += 1
  if char in "Ii":
    counti += 1
  if char in "Oo":
    counto += 1
  if char in "Uu":
    countu += 1
print(f"There are {counta:.0f} a's.")
print(f"There are {counte:.0f} e's.")
print(f"There are {counti:.0f} i's.")
print(f"There are {counto:.0f} o's.")
print(f"There are {countu:.0f} u's.")

count = 0
for i in string:
    if i not in "AaEeIiOoUu":
        count += 1
print(f"There are {count} non-vowels characters.")
