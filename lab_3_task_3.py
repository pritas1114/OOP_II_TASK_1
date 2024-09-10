# -*- coding: utf-8 -*-
"""Lab_3_Task_3

Use Colab.

Original file is located at
    https://colab.research.google.com/drive/1rWdERWINnTVmuTVxbMMCUnmSP7f1kOQM
"""

#lab 03 // task 03
# Set Operations

a = {1,3,5,8,5,2}
b = {0,False,1,5}
print(len(a), type(a))
print(len(b), type(b))
a.add(10)
print(a)
a.discard(8)
print(a)
union_set = a.union(b)   # Union
intersection_set = a.intersection(b)  # Intersection
difference_set = a.difference(b)   # Difference
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)

for item in a:
    if item == 5:
        break
    print(item)
c={2,3,4}
d=a.union(c)
print(d)
