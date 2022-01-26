import sys
score = input("Enter numeric value of score: ")
try:
    score = float(score)
    if score > 1.0:
        print ("Bad score")
        #print letter grade
    elif 1.0 >= score>=.9:
        print ("A" + str(score))
    elif .9 > score>=.8:
        print("B")
    elif .8 > score>=.7:
        print("C")
    elif .7 > score>.6:
        print("D")
    elif .6 > score>=.5:
        print("F")
except valueError:
    print("You need to input a number")
#program is End
