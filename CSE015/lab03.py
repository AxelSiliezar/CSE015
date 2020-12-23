from logic import *

# input goes here
#for a composed one i has to be in the following format: p and q,a -> q
#the comma is very important if not, the program would break
#Also the placement of the comma is very important. check example above
x = [x for x in input("Enter the parameters : ").split(",")]
print("The value selected is ", x)
#transform the t-table
mytable = TruthTable(x)
mytable.display()
mainTable = mytable.table
finalNumbers = []
#append the numbers
for numbers in mainTable:
    finalNumbers.append(numbers[1][0])

#verify the numbers being appended with print(finalnumbers)

#Filter for last numbers
if all(items == 0 for items in finalNumbers):
    print("It is a Contradiction")
elif all(items == 1 for items in finalNumbers):
    print("It is a Tautology")
else:
    print("It is a Contingency")
