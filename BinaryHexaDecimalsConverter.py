print("Binary Hexadecimal Converter App")

print("\nConvert Your decimals to binary and hexadecimals.")
input_max_value = int(input("Enter a number: "))

decimals = range(1, input_max_value+1)
binary_values = []
hexadecimal_values = []

for num in decimals:
    binary_values.append(bin(num))
    hexadecimal_values.append(hex(num))

print("Processing the conversions.. .")
print("First, we will show you a slice of the numbers\n")

lower = int(input("Please enter a starting number: "))
higher = int(input("Please enter a ending number: "))

print("\nA sample of Binary Values")
for num in binary_values[lower:higher]:
    print(num)

print("\nA sample of Hexadecimal Values")
for num in hexadecimal_values[lower:higher]:
    print(num)

input("Press enter to view the complete list of values: ")
print("Decimals - - Binary - -  Hexadecimals")
for d, b, h in zip(decimals, binary_values, hexadecimal_values):
    print(f"{d}   {b}    {h}")


print("\nThank you!")