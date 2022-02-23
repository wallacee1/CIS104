def count():

    fruit = input("Enter a fruit:")
    alpha = input("Enter a letter:")

    word = fruit
    count = 0
    for letter in word:
        if letter == alpha:
            count = count + 1
    print(count)

count()