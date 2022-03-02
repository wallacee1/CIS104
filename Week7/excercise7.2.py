fname = input('Enter the file name: ')
fhand = open(fname)
total = 0
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        #print(line)
        num = float(line[20:])
        total = total + num
        count = count + 1
        avg = total / count
print('Average spam confidence: ', avg)

