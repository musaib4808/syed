n = input("Enter a number: ")
power = len(n)
total = sum(int(digit)**power for digit in n)

print("Armstrong Number" if total == int(n) else "Not an Armstrong Number")