#Lab: 03 Task: 01

a = (1,3,5,7,4)

print(len(a))

print(type(a))

print(a[-2])

print(a[2])

b = list (a)
b[-3] = 50
a = tuple(b)
print(a)

print(a[-4 : -1])


b = list (a)
b [2] = 100
b.append(100)
a = tuple(b)
print(a)

b = list (a)
b [2] = 400
b.append(400)
a = tuple(b)
print(a)

b = list (a)
b.remove(1)
a = tuple(b)
print(a)


c = (2,4,6)
d=a+c
print(d)


d = (3, 100, 7, 4, 400, 2, 4, 6)
b = sorted(d)
sorted_tuple = tuple(b)
print(sorted_tuple)


e = ("3", "100", "7", "4", "400", "2", "4", "6")
for i in range(len(e)):
  print(e[i])
