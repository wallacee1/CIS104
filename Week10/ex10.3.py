import string

counts = 0
dcounts = dict()
lst = list()

fname = input("Enter File Name:")
try:
    fhand = open(fname)
except FileNotFoundError:
    print("File Not Found")
    exit()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()

    words = line.split()
    for word in words:
        for letter in word:
            counts +=1
            if letter not in dcounts:
                dcounts[letter] = 1
            else:
                dcounts[letter] += 1
for key, val in list(dcounts.items()):
    lst.append((val, key))

lst.sort(reverse = True)

for key, val in lst:
    print(val, key)