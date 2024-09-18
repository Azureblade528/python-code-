sentence = "Python is fun"
sentence_words = sentence.split()
length = []

for i in sentence_words:
    length.append(len(i))
print(length)
