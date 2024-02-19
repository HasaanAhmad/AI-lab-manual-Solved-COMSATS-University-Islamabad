# LAB 3 (HASAAN AHMAD SP22-BSE-017 )

from math import *
h = 0.001
x_values = []
for i in range(int(-pi/h), int(pi/h) + 1):
    x_values.append(i * h)

def derivative_of_sin(x, h):
    return (sin(x + h) - sin(x)) / h

for x in x_values:
    derivative = derivative_of_sin(x, h)
    actual_cos = cos(x)
    print(f"At x = {x}, Derivative of sin(x) = {derivative}, Cos(x) = {actual_cos}")
