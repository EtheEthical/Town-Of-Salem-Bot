from random import randint as r

def randint(a, b):
    list = []
    for i in range(1000):
        list.append(r(a, b))



    return list[r(0, len(list)-1)]

'''
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0


list = []

for sixseven in range(10000):
    list.append(randint(1, 10))


for i in range(len(list)):
    if list[i] == 1:
        one = one + 1
    elif list[i] == 2:
        two = two + 1
    elif list[i] == 3:
        three = three + 1
    elif list[i] == 4:
        four = four + 1
    elif list[i] == 5:
        five = five + 1
    elif list[i] == 6:
        six = six + 1
    elif list[i] == 7:
        seven = seven + 1
    elif list[i] == 8:
        eight = eight + 1
    elif list[i] == 9:
        nine = nine + 1
    elif list[i] == 10:
        ten = ten + 1


print(f"One: {one}")
print(f"Two: {two}")
print(f"Three: {three}")
print(f"Four: {four}")
print(f"Five: {five}")
print(f"Six: {six}")
print(f"Seven: {seven}")
print(f"Eight: {eight}")
print(f"Nine: {nine}")
print(f"Ten: {ten}")

'''

