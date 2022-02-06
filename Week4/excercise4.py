def high(x, y, z):
    nums = [x, y, z]
    return max(nums)


x = int(input("Enter a number:"))
y = int(input("Enter another number:"))
z = int(input("And one more number:"))

print("Highest number is:", high(x, y, z))