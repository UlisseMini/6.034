# This is the file you'll use to submit most of Lab 0.

# Certain problems may ask you to modify other files to accomplish a certain
# task. There are also various other files that make the problem set work, and
# generally you will _not_ be expected to modify or even understand this code.
# Don't get bogged down with unnecessary work.


# Section 1: Problem set logistics ___________________________________________

# This is a multiple choice question. You answer by replacing
# the symbol 'fill-me-in' with a number, corresponding to your answer.

# You get to check multiple choice answers using the tester before you
# submit them! So there's no reason to worry about getting them wrong.
# Often, multiple-choice questions will be intended to make sure you have the
# right ideas going into the problem set. Run the tester right after you
# answer them, so that you can make sure you have the right answers.

# What version of Python do we *recommend* (not "require") for this course?
#   1. Python v2.3
#   2. Python v2.5 or Python v2.6
#   3. Python v3.0
# Fill in your answer in the next line of code ("1", "2", or "3"):

# python2 is cringe, so I'm using python3 screw you
ANSWER_1 = '2'


# Section 2: Programming warmup _____________________________________________

# Problem 2.1: Warm-Up Stretch

def cube(x):
    return x**3

# I know they want a recursive solution, but that's retarded.
def factorial(x):
    if x < 0:
        return ValueError('factorial({x})'.format(x=x))
    acc = 1
    for n in range(1, x+1):
        acc *= n
    return acc

def count_pattern(pattern, lst):
    matches = 0

    # for i in range(0, len(lst)-len(pattern)+1):
    i = 0

    # since x[a:b] excludes b, we add one to the right hand side.
    while i < len(lst) - len(pattern) + 1:
        if lst[i:i+len(pattern)] == pattern:
            matches += 1
        i += 1

    return matches

# not part of the lab, but I like to test my code...
n = count_pattern(('a', 'b'), ('a', 'b', 'c', 'd', 'b', 'a', 'b', 'f'))
assert n == 2, n

n = count_pattern(('a', 'b', 'a'), ('g','a','b','a','b','a','b','a'))
assert n == 3, n

assert factorial(3) == 6
assert factorial(4) == 24


# Problem 2.2: Expression depth

def depth(expr):
    if isinstance(expr, (list, tuple)):
        return 1 + max(depth(subexpr) for subexpr in expr)
    else:
        return 0


assert depth('x') == 0
assert depth(('expt', 'x', 2)) == 1
d = depth(
    ('+',
     ('expt', 'x', 2),
     ('expt', 'y', 2)))
assert d == 2, d

d = depth(
    ('/',
     ('expt', 'x', 5),
     ('expt', ('-',
               ('expt', 'x', 2), 1),
               ('/', 5, 2))))
assert d == 4, d

# Problem 2.3: Tree indexing

def tree_ref(tree, index):
    for i in index:
        tree = tree[i]
    return tree


tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))
tr = tree_ref(tree, (3, 1))
assert tr == 9, tr

tr = tree_ref(tree, (1, 1, 1))
assert tr == 6, tr

# Section 3: Symbolic algebra

# Your solution to this problem doesn't go in this file.
# Instead, you need to modify 'algebra.py' to complete the distributer.

from algebra import Sum, Product, simplify_if_possible
from algebra_utils import distribution, encode_sumprod, decode_sumprod

# Section 4: Survey _________________________________________________________

# Please answer these questions inside the double quotes.

# When did you take 6.01?
WHEN_DID_YOU_TAKE_601 = ""

# How many hours did you spend per 6.01 lab?
HOURS_PER_601_LAB = ""

# How well did you learn 6.01?
HOW_WELL_I_LEARNED_601 = ""

# How many hours did this lab take?
HOURS = ""
