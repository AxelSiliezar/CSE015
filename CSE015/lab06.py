# creates the domain
A = {'dog', 'cat', 'fish', 'frog'}
# creates the codomain
B = {1, 2, 3, 4, 5, 6}

# creates the graph of a function
f = {('dog', 1), ('cat', 1), ('frog', 5), ('fish', 4)}
# This corresponds to the following function
# f(dog) = 1
# f(cat) = 1
# f(frog) = 5
# f(fish) = 4

# creates the domain
D = {'dog', 'cat', 'fish', 'frog'}
# creates the codomain
E = {1, 2, 3, 4, 5, 6}

# creates the graph of a function
q = {('dog', 2), ('cat', 3), ('frog', 5), ('fish', 1)}

# prints domain and codomain as sets
print('Domain A')
print(A)
print('Codomain B')
print(B)

# prints the graph of the function as a set
print('Graph of the function')
print(f)


def equal_func(first, second):
    if first == second:
        return True
    else:
        return False


checker = equal_func(f, q)
if checker:
    print('Functions are equal')
else:
    print('Functions are not equal')


def partial_func(param, secondparam):
    if param != secondparam:
        return True
    else:
        return False


secondChecker = partial_func(A, f)
if secondChecker:
    print('Partial function')
else:
    print('Not a partial function')


def compos_func(firstparam, secondparam):
    empty = []
    for one in firstparam:
        for two in secondparam:
            if one[1] == two[0]:
                empty.append({[one[0], two[1]]})
    return empty


ownFunct = compos_func(A, D)
print(ownFunct)
