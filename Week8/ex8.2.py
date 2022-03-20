#Eric Wallace
#Excercise 8.2

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    if len(words[2]) > 3 :
        print(words[3])
    else :
        print(words[2])