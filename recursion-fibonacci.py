"""
Consider a number sequence:

1 1 2 3 ...

Each subsequent number is the sum of the two preceding numbers. 
Your task is to find the M term in the sequence based on the given input.

Testcase 1
Input: 5
Output: 5

Testcase 2
Input: 6
Output: 8

"""

# First idea (kinda long ;9 but still works :D)
"""M = int(input())

old = 0
current = 1
new = 0

def recur(old, current, new):
    new = current + old
    current = old
    old = new
    return old, current, new

for i in range(0, M):
    old, current, new = recur(old, current, new)

print(new)"""

# Second idea
def helpmeh(M):
    first, second = 0, 1
    for _ in range(M):
        first, second = second, first+second #replace the first with second for next step and make new second value
    return first

M = int(input())
print(helpmeh(M))
