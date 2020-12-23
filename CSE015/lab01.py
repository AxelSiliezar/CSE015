# Part 1
name = input('Please tell me your name to begin: ')
print("Hello", name)
# Part 2
numberInput = int(input("Please enter a number to determine if it is even or odd, {}: ".format(name)))

modifier = numberInput % 2
if modifier > 0:
    print("The number is odd")
else:
    print("The number is even")

# part 3
oddCount = 0
for opts in range(10):
    attempt = int(input("Enter an integer, {}: ".format(name)))
    if attempt % 2 == 1 and (oddCount == 0 or attempt > oddCount):
        oddCount = attempt

if oddCount:
    print("Maximum odd entered was", oddCount)
else:
    print("No odd numbers were entered")

# Axel Siliezar - CSE 15 - Fall 2020
