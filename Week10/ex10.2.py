dhours = dict()
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
    hpos = words[5].find(':')
    hour = words[5][:hpos]
    if hour not in dhours:
        dhours[hour] = 1
    else:
        dhours[hour] += 1

for key, val in list(dhours.items()) :
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)