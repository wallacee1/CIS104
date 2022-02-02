def computepay(hours, rate):
    print("In computepay", hours, rate)
    if hours > 40 :
        total = 40 * rate
        overtime = hours - 40
        overtimePay = overtime * (rate * 1.5)
        pay = total + overtimePay

    else:
        pay = hours * rate

    return(pay)


try :
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except :
    print("Error, please enter numeric input")
    quit()

total = computepay(hours, rate)

print("Pay:",total)