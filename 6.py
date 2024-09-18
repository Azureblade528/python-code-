def flat(nested_list):
    for i in nested_list:
        if isinstance(i, list):
            flat(i)
        else:
            flatn.append(i)


flatn = []
nested_list = [1, [2, [3, 4], 5], 6]
flat(nested_list)
print(flatn)
