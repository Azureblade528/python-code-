n1 = "Listen"
n2 = "Silent"
n1 = n1.lower()
n2 = n2.lower()
list1 = list(n1)
list2 = list(n2)
list1.sort()
list2.sort()
if (list1 == list2):
    print("Anagram")
else:
    print("Not an anagram")
