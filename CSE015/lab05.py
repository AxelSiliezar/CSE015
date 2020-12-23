# This is the first function
A = {'hello', 'world', '!'}
B = {1, 2, 3, 4, 5, 6}
f = {('Hello', 1), ('World', 2), ('!', 3)}

print('Domain A')
print(A)

print('Codomain B')
print(B)

print('Subset of A x B')
print(f)


def is_a_graph(A, B, f):
    for counter in f:
        a = counter[0]
        b = counter[1]
        for index in f:
            if index != counter:
                checker = index[0]
                if a == checker:
                    return False
    return True


check = is_a_graph(A, B, f)
if check == True:
    print('This is a graph')
else:
    print('Not a graph')


# This is the second function

def is_surjective(A, B, f):
    for counterElement in B:
        b = counterElement
        count = 0
        for index in f:
            count = count + index.count(b)
        if count == 0:
            return False
    return True

cheksur = is_surjective(A,B,f)
if cheksur == True:
    print(' Function is surjective')
else:
    print('Not a surjective function.')
