

"""
number = int(input())

s = set()

for i in range(number):
    c = str(input())
    s.add(c)


print((s))
"""



n = int(input())
new_list = []
for i in range(n):
    print(i)
    countriename = input()
    new_list.append(countriename)
    print(new_list)


print(set(new_list))

