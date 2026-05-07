n = int(input("Enter a number: "))
for i in range(2, n):
    if n % i == 0: n = 0; break
print("Prime Number" if n > 1 else "Not a Prime Number")