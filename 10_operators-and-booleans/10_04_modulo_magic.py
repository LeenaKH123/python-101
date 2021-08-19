# Use the modulo operator to confirm which of the values
# shown below are divisible by seven.

num_1 = 42
num_2 = 137
num_3 = 455
num_4 = 1997

res1 = num_1 % 7
res2 = num_2 % 7
res3 = num_3 % 7
res4 = num_4 % 7

if res1 == 0:
    print("This number is divisible by 7:", num_1)
if res2 == 0:
    print("This number is divisible by 7:", num_2)
if res3 == 0:
    print("This number is divisible by 7:", num_3)
if res4 == 0:
    print("This number is divisible by 7:", num_4)
