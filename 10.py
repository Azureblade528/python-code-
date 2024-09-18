dictionaries = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Doe", "age": 40}
]
sorted_dictionaries = sorted(dictionaries, key=lambda x: x["age"])
print(sorted_dictionaries)
