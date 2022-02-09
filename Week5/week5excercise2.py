num = 0
tot = 0.0
largest = None
smallest = None
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = sval
    elif sval > largest:
        largest = sval
    if smallest is None:
            smallest = sval
    elif sval < smallest:
            smallest = sval
    # print(fval)
    num = num + 1
    tot = tot + fval

print('ALL DONE')
print(tot,num,smallest,largest)