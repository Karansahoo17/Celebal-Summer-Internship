# 1. py-if-else
"""
This task uses conditional statements to decide output based on the value of input.
The `if`, `elif`, and `else` statements allow branching logic.
You can use them to evaluate conditions and respond accordingly.
"""
n = 7
if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

# Example:
# n = 3 => Output: Weird
# n = 24 => Output: Not Weird

# 2. python-arithmetic-operators
"""
This task involves basic math operations like addition, subtraction, and multiplication.
Operators used: +, -, *
"""
a, b = 10, 5
print(a + b)  # 15
print(a - b)  # 5
print(a * b)  # 50

# 3. compress-the-string
"""
This compresses a string using groupby from itertools, 
which groups consecutive characters and counts them.
"""
from itertools import groupby
s = "1222311"
for key, group in groupby(s):
    print(f"({len(list(group))}, {key})", end=' ')
# Output: (1, 1) (3, 2) (1, 3) (2, 1)

# 4. the-minion-game
"""
Two players (Kevin and Stuart) compete by forming substrings.
Kevin gets points for substrings starting with vowels, Stuart with consonants.
Points = number of times substring appears.
"""
def minion_game(string):
    vowels = 'AEIOU'
    kevin = stuart = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

minion_game("BANANA")  # Output: Stuart 12

# 5. write-a-function
"""
Functions help define reusable blocks of logic.
Use `def` keyword to define a function.
Example below checks if a year is a leap year.
"""
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap(2000))  # True
print(is_leap(1900))  # False

# 6. word-order
"""
Counts frequency of words from input while preserving their order of appearance.
Use OrderedDict or a regular dict in Python 3.7+ (which maintains insertion order).
"""
from collections import OrderedDict
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
d = OrderedDict()
for word in words:
    d[word] = d.get(word, 0) + 1
print(len(d))        # 3
print(*d.values())   # 3 2 1

# 7. iterables-and-iterators
"""
Uses itertools.combinations to find probability that at least one 'a' is in a random combination.
Good practice in using iterators, generators, and combinatorics.
"""
from itertools import combinations
letters = ['a', 'b', 'c', 'a']
k = 2
comb = list(combinations(letters, k))
a_count = sum(1 for c in comb if 'a' in c)
print(f"{a_count/len(comb):.4f}")  # Output: 0.8333

# 8. python-tuples
"""
Tuples are immutable sequences. Useful for hashing and fixed data structures.
Can be passed to hash() to get a unique identifier.
"""
n = 3
integer_list = (1, 2, 3)
print(hash(integer_list))  # Outputs a hash value

# 9. finding-the-percentage
"""
Stores names and scores in a dictionary, retrieves and computes average for queried student.
Demonstrates use of dict and formatting output to 2 decimal places.
"""
students = {
    "John": [70, 80, 90],
    "Alice": [88, 76, 92],
    "Bob": [60, 65, 70]
}
query_name = "Alice"
average = sum(students[query_name])/len(students[query_name])
print(f"{average:.2f}")  # Output: 85.33

# 10. python-string-formatting
"""
Demonstrates formatting of numbers in different bases (binary, octal, hexadecimal).
String formatting helps in aligning clean outputs.
"""
def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        print(str(i).rjust(width), oct(i)[2:].rjust(width), hex(i)[2:].upper().rjust(width), bin(i)[2:].rjust(width))

print_formatted(5)
# Output:
#   1   1   1   1
#   2   2   2  10
#   3   3   3  11
#   4   4   4 100
#   5   5   5 101
