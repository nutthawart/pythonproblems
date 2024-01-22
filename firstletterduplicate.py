"""
Write a Python function to solve quadratic equation in the form Ax^2 + Bx + C = 0.
Given A, B and C
The function should return answer for that equation
If there's no answer should return NAN

Testcase 1
Input:
1
6
8

Output:
-2
-4

Testcase 2
Input:
1
4
6

Output:
NAN

"""
import math

A = int(input())
B = int(input())
C = int(input())

# formula to easily solve quadratic equation (yk that -b+-sqrt kinda thing)
try:
    print(((-B)+(math.sqrt((B**2)-(4*A*C))))/2*A)
    print((((-B)-(math.sqrt((B**2)-(4*A*C))))/2*A))
except:
    ValueError
    print("NAN")

