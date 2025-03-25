num = int(input("Enter a number: "))
total = sum(int(digit) for digit in str(num))
print(f"Sum of the digits: {total}")
