string = input("Enter a sentence ")
counts = dict()
words = string.split()

longest = len(max(words, key=len))

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

for key in sorted(counts):
    print("{:{}}: {}".format(key, longest, counts[key]))
