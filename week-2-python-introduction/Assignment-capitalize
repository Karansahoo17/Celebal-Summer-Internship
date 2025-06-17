# 11. capitalize
"""
Converts the first letter of every word in a string to uppercase.
This is useful when formatting names or sentences.
Python provides a built-in method `.title()` and string manipulation can also be used.
"""
def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

print(capitalize_words("hello world"))  # Hello World
print(capitalize_words("python programming"))  # Python Programming

# 12. py-introduction-to-sets
"""
Calculates the average of unique values in a list using a set.
Sets automatically remove duplicates, making them perfect for such tasks.
"""
def average(array):
    return sum(set(array)) / len(set(array))

print(average([1, 2, 3, 4, 5]))  # 3.0
print(average([1, 1, 2, 2, 3]))  # 2.0

# 13. text-wrap
"""
Wraps text to a specified width using the `textwrap` module.
Very useful for formatting outputs to fit within a terminal or UI.
"""
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))

# 14. alphabet-rangoli
"""
Prints an alphabet rangoli pattern using string manipulation and padding.
Great for practice with loops, string joining, and formatting.
"""
def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    lines = []
    for i in range(size):
        s = "-".join(alpha[size-1:i:-1] + alpha[i:size])
        lines.append(s.center(4*size-3, "-"))
    print("\n".join(lines[::-1] + lines[1:]))

print_rangoli(3)

# 15. merge-the-tools
"""
Splits a string into parts of given length and removes duplicate characters from each part.
Handy for breaking and compressing strings.
"""
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        seen = ""
        for c in string[i:i+k]:
            if c not in seen:
                seen += c
        print(seen)

merge_the_tools("AABCAAADA", 3)

# 16. collections-counter
"""
Calculates the total income from shoe sales based on customer requests.
Uses Counter to manage inventory.
"""
from collections import Counter

inventory = Counter([2, 3, 4, 5, 6, 8, 7, 6, 5, 18])
customers = [(6, 30), (6, 40), (6, 50), (18, 60), (10, 20)]
income = 0
for size, price in customers:
    if inventory[size]:
        income += price
        inventory[size] -= 1
print(income)  # Output: 150

# 17. exceptions
"""
Demonstrates exception handling using try-except blocks.
Used to catch and handle errors without stopping the program.
"""
tests = [(1, 0), (2, "a"), (3, 1)]
for a, b in tests:
    try:
        print(int(a) // int(b))
    except Exception as e:
        print("Error:", e)

# 18. incorrect-regex
"""
Checks if a string is a valid regex pattern using try-except.
Useful when validating user-defined patterns.
"""
import re
patterns = [".*", "[a-z]+", "[", "[A-Z]{"]
for pattern in patterns:
    try:
        re.compile(pattern)
        print(True)
    except re.error:
        print(False)

# 19. py-set-discard-remove-pop
"""
Demonstrates set operations: discard(), remove(), and pop().
- discard(x): Removes x if present, no error if not.
- remove(x): Removes x, raises error if not present.
- pop(): Removes arbitrary item from set.
"""
s = set([1, 2, 3, 4, 5])
s.discard(3)
s.remove(4)
s.pop()
print(s)  # Remaining set
