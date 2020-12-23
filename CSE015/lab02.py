from logic import *

# myTable = TruthTable(['p', 'q'], ['p or q'])
# myTable.display()
# myTable.latex()

# secondTable = TruthTable(['p', 'q'], ['p or q', 'p and q'])
# secondTable.latex()
# secondTable.display()
# Warm Up
warmUp1 = TruthTable(['a', 'b'], ['a and -b'])
warmUp1.display()
print()

warmUp2 = TruthTable(['a', 'b', 'c'], ['(a and b) or -c'])
warmUp2.display()
print()
# Tautologies, print statements just to create space and make it cleaner.
firstTable = TruthTable(['p', 'q'], ['((p -> q) and q) -> q'])
firstTable.display()
print()
firstTable.latex()
print()

secondTable = TruthTable(['p', 'q'], ['(-q and (p -> q)) -> -q'])
secondTable.display()
print()
secondTable.latex()
print()

thirdTable = TruthTable(['p', 'q', 'r'], ['((p -> q ) and (q -> r)) -> (p -> r)'])
thirdTable.display()
print()
thirdTable.latex()
print()

fourthTable = TruthTable(['p', 'q', 'r'], ['((p or q) and -p) -> q'])
fourthTable.display()
print()
fourthTable.latex()
print()

fifthTable = TruthTable(['p', 'q'], ['p -> (p or q)'])
firstTable.display()
print()
fifthTable.latex()
print()

sixthTable = TruthTable(['p', 'q'], ['(p and q) -> p'])
sixthTable.display()
print()
sixthTable.latex()
print()

seventhTable = TruthTable(['p', 'q'], ['((p) and (q)) -> (p and q)'])
seventhTable.display()
print()
seventhTable.latex()
print()

eightTable = TruthTable(['p', 'q', 'r'], ['((p or q) and (-p or r)) -> (q or r)'])
eightTable.display()
print()
eightTable.latex()
print()
