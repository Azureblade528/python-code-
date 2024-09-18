list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
intersection = []
for i in list1:
    for n in list2:
        if (i == n):
            intersection.append(i)
print(intersection)
