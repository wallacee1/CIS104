def computegrade(score):
    if (score > 1) or  (score < 0) :
        message = ("Bad score")
        quit()
    elif score >= .9 :
        message = ("A")
    elif score >= .8 :
        message = ("B")
    elif score >= .7 :
        message = ("C")
    elif score >= .6 :
        message = ("D")
    else :
        message = ("F")
    return(message)

try :
    score = float(input("input score: "))
except :
    print("that is not a number please use numeric input")
    quit()
grade = computegrade(score)
print(grade)