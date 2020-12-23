print('Recursively defined function')
def compute_f(n):
    if n == 0:
        return 2
    return compute_f(n - 1) + 2


# test
response = "y"
while response[0].lower() == "y":
    number = int(input("Value for n: "))
    print('Result: ', compute_f(number))
    response = input('Do another (y/n)? ')

print('Counting the number of occurrences of an element in a list')
def count_instances(L, n):
    if len(L) == 0:
        return 0
    if L[0] == n:
        return 1 + count_instances(L[1:], n)
    else:
        return count_instances(L[1:], n)


# test
List = [4, 5, 9, 7, 7, 1, 9, 7, 2]
print('List: ', List)
print('Result: ', count_instances(List, 4))
print('Result: ', count_instances(List, 7))
print('Result: ', count_instances(List, 3))
print('Result: ', count_instances(List, 9))
