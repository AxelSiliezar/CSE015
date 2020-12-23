import random
import time
import sys

sys.setrecursionlimit(10 ** 9)
""" 
THIS CODE ALLOWS SINGLE SEARCH FOR EFFICIENCY OF THE COMPUTER AND FAST PERFORMANCE.

IT RUNS IN A LOOP TO SEARCH MANUALLY IN CASE A DIFFERENT NUMBER IS DESIRE AND TO AVOID 
TOLL IN THE COMPUTER.

"""


def gen_random_list(n):
    """
    Generates a list with n non-negative random integers

    Parameters
    ----------
    n : int
        Number of elements in the list. Must be positive.

    Returns
    -------
    List with n non-negative random integers

    """

    assert (n > 0)
    l = [random.randint(0, 10 * n) for _ in range(n)]
    return l


def linear_search(s, k):
    for i in range(len(s)):
        if s[i] == k:
            return i


def binary_search(s, k):
    if len(s) == 1:
        if s[0] == k:
            return 0
        else:
            return -1
    else:
        mid = int(len(s) / 2)
        if s[mid] == k:
            return mid
        elif s[mid] > k:
            first_answer = binary_search(s[:mid], k)
            if first_answer == -1:
                return -1
            else:
                return first_answer
        else:
            second_answer = binary_search(s[mid:], k)
            if second_answer == -1:
                return -1
            else:
                return second_answer + mid


if __name__ == '__main__':
    response = "y"
    while response[0].lower() == "y":
        n = int(input("Enter number (ex. 10, 100, 1000): "))

        print("Linear Search Time:")
        print('Searching...')
        l = gen_random_list(n)
        start_time = time.perf_counter()
        linear_search(l, -4)
        spent_time = time.perf_counter() - start_time
        print("Time spent is ", spent_time)

        print("-------------------------------------------")

        print("Binary Search Time:")
        print('Searching...')
        l = gen_random_list(n)
        start_time = time.perf_counter()
        binary_search(l, -4)
        spent_time = time.perf_counter() - start_time
        print("Time spent is ", spent_time)
        response = input('Do another (y/n)? ')
