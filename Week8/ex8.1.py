#Eric Wallace
#Excercise 8.1

words = ['a', 'b', 'c']

def chop() :
    words.remove(words[(len(words) - 1)])
    return words.remove((words[0]))

def middle() :
    wordsCool = []
    wordsCool.extend(words)
    wordsCool.remove(wordsCool[(len(wordsCool) - 1)])
    wordsCool.remove((wordsCool[0]))
    return wordsCool


print("Middle Function: ")
print(middle())
#print(words)

print("Chop Function: ")
print(chop())
#print(words)