name = list(input("Enter the string"))
print(name)
count_dictonary = {}

for each_letter in name:

    count_dictonary[each_letter] = name.count(each_letter)

print(count_dictonary)

