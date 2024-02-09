import math  # import module for Python

# Calc the circle area:
radius = float(input('Enter the radius for your area: '))
area = math.pi * radius ** 2
print(f"Circle area = number_pi * radius^2 = {math.pi:.2f} * {radius:.2f}^2 = {area:<,.2f}")

# Calc the number Fibonacci
n = int(input('Enter the serial number for number Fibonacci (n): '))
phi = 1.618
F_n = (phi**n - (1 - phi)**n)/math.sqrt(5)
print(f"Number Fibonacci for this serial number = (phi^n - (1 - phi)^n)/math.sqrt(5) = (1.618^{n} - (1 - 1.618)^{n}/"
      f"{int(math.sqrt(5))} = {F_n}")