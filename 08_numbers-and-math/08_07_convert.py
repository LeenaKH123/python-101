# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?
integer = 5
print(integer, "is of type:", type(integer))

integer_converted = float(integer)
print(integer_converted, "is of type:", type(integer_converted))

float = 5.5
print(float, "is of type:", type(float))

float_converted = int(float)
print(float_converted, "is of type:", type(float_converted))

division_float_int = 6.0 / 5
print("divide a float by an integer", division_float_int)

multiplication = 5.0 * 8
print("two variables multiplication", multiplication)
