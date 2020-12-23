mySet = set()
response = 'y'
while response.lower() == 'y':
    option = input('Enter one more element ? [Y/N] ')
    if option == 'N'.lower():
        break
    val = int(input('Enter the new element in the set: '))
    mySet.add(val)
print(mySet)