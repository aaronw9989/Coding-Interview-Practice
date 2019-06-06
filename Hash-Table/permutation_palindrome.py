
from collections import defaultdict





def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome

    dic = defaultdict(int)

    for char in the_string:
        dic[char] += 1

    num_odd_chars = 0

    for char in dic:
        if dic[char] % 2 != 0:
            num_odd_chars += 1

    if num_odd_chars <= 1:
        return True

    return False