# Coverting an Integer into Decimal
int_num = 23
new_num = float(int_num)
print(new_num)
print(type(new_num))

# But above code is wrong because float values are stored in binary(base-2) format.
# They store an approximation of most real numbers, not the exact value.
# Use Cases: Ideal for scientific calculations and graphics where performance is critical 
# and some degree of approximation is acceptable.

import decimal
integer = 10
print(decimal.Decimal(integer))
print(type(decimal.Decimal(integer)))

# This above code is correct because Decimal type stores numbers interally using a decimal (base-10) format or a scaled integer, precisely matching how humans write them.
# it provides exact representation exact representation for numbers that are terminating decimals within its range and defined precision, avoiding the binary rounding issues.
# Use Cases: Essential for financial applications, currency amounts, and other scenarios where exact decimal precision and the prevention of rounding errors are critical.