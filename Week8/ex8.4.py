#Eric Wallace
#Excercise 8.4

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.rstrip().split()
    for uniques in words:
        if uniques in lst:
            continue
        else:
            lst.append(uniques)
lst.sort()
print(lst)
