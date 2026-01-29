a = 7
b = 2

# Arithmetic Operators
print("Arithmetic Operators")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")   # Float division for clarity
print(f"{a} % {b} = {a % b}\n")

# Relational Operators
print("Relational Operators")
print(f"{a} < {b} = {a < b}")
print(f"{a} > {b} = {a > b}")
print(f"{a} == {b} = {a == b}")
print(f"{a} != {b} = {a != b}\n")

# Logical Operators
print("Logical Operators")
print(f"AND {a} and {b} = {bool(a and b)}")
print(f"OR {a} or {b} = {bool(a or b)}")
print(f"NOT {a} = {not a}\n")

# Bitwise Operators
print("Bitwise Operators")
print(f"{a} & {b} = {a & b}")
print(f"{a} | {b} = {a | b}")
print(f"Bitwise XOR {a} ^ {b} = {a ^ b}")
print(f"Left Shift {a} << 2 = {a << 2}")
print(f"Right Shift {a} >> 2 = {a >> 2}")

# Conditional (Ternary) Operator
print("\n" + ("a is greater than b" if a > b else "b is less than a"))

# OUTPUT
Arithmetic Operators
7 + 2 = 9
7 - 2 = 5
7 * 2 = 14
7 / 2 = 3.50
7 % 2 = 1

Relational Operators
7 < 2 = False
7 > 2 = True
7 == 2 = False
7 != 2 = True

Logical Operators
AND 7 and 2 = True
OR 7 or 2 = True
NOT 7 = False

Bitwise Operators
7 & 2 = 2
7 | 2 = 7
Bitwise XOR 7 ^ 2 = 5
Left Shift 7 << 2 = 28
Right Shift 7 >> 2 = 1

a is greater than b

=== Code Execution Successful ===
