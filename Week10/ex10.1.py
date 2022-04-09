daddress = dict()
lst = list()

fname = input("Enter File Name:")
try:
    fhand = open(fname)
except FileNotFoundError:
    print("File Not Found")
    quit()
for line in fhand :
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in daddress :
            daddress[words[1]] = 1
        else :
            daddress[words[1]] += 1
for key, val in list(daddress.items()) :
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:1]:
    print(val, key)