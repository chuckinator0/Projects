'''This file was given to me by an alum at Insight Data Science'''

""" Python data structures. """

# Boolean

bool, True                      #I Boolean

# Numeric

int     , 1                     #I Integer
float   , 1.0                   #I Floating point
complex , (1+0j)                #I Complex

# Sequences

str   , '123'                   #I String
tuple , (1, 2, 3)               #I Tuple
list  , [1, 2, 3]               #M List
bytes , b'\x00'                 #I Bytes


# Mappings

dict, {1: 1}                    #M Dictionary

# Sets

set      , {1, 2, 3}            #M Set
frozenset, frozenset({1, 2, 3})   #I Frozen Set



""" Mutability of objects (changeable in place) """

# E.g. 1 -- Variable assignment.

# Immutable
a = '1'
b = a
a += '2'

a
'12'
b
'1'

# Mutable
a = [1]
b = a
a.append(2)

a
[1, 2]
b
[1, 2]


# E.g. 2 -- Dictionaries. Keys must be immutable.

# Keys must be immutable (hashable) objects

# Allowed               # TypeError: unhashable type
d = {  1: 1}            d = {  [1]: 1}
d = {'a': 1}            d = {   {}: 1}
d = {int: 1}            d = {set(): 1}



""" The truthyness of objects """

# Determine truthyness for any kind of object or statement.

bool(1 > 0) 
bool(object())

# Class             # True              # False
int,                1, 2, 9999,         0
float,              0.1, 0.2, 1e3,      0.0
str,                'a', 'ab',          ''
tuple,              (1,), ('a'),        ()
list,               [1],  ('a'),        []
dict,               {1: 1},            {}
set,                set([1]),           set()

# E.g. 1

variable = 0

# Fine
if variable > 0:
    print(variable)

# Better
if variable:
    print(variable)


# E.g. 2

variable = []

# Fine
if len(variable) > 0:
    print(variable)

# Better
if variable:
    print(variable)



""" Helpful exploration functions. """

# Command       # Usage  
help,           help(object)        # The docstring for that object.
dir,            dir(object)         # The methods and properties of an object.
type,           type(object)        # The type of the object.



""" Sequence reshaping """


# Flatten a list or tuple.

l1 = [[1, 2], [3, 4]]
l2 = ((1, 2), (3, 4))

l1 = sum(l1, [])
l2 = sum(l2, ())

l1
[1, 2, 3, 4]
l2
(1, 2, 3, 4)


# Zip -- Combine list elements pair-wise.

l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]

for i, j in zip(l1, l2):
    i, j

'a', 1
'b', 2
'c', 3

# Zip -- reshape a list.

l = [1, 2, 3, 4, 5, 6]

l2 = zip(*[iter(l)] * 2)

l2
[(1, 2), (3, 4), (5, 6)]






""" List, Dictionary, Generator, and Set Comprehensions. """


# List

l = []
for number in range(3):
    l.append(number)

l = [number for number in range(3)]

# Dictionary

d = {}
for key, value in zip('123', range(3)):
    d[key] = value

d = {key : value for key, value in zip('123', range(3))}

# Generator

def generator(n=3):
    i = 0
    while i < n:
        yield i
        i += 1

g = generator(3)

g = (i for i in range(3))

# Set

s = set()
for i in range(3):
    s.update([3])

s = {i for i in range(3)}



""" List modifications with map, filter, and reduce. """

# Map -- map a function to a list

l1 = ['1', '2']

# Fine.
l2 = []
for element in l1:
    l2.append(int(element))

# Better
l2 = map(int, l1)


# Better.
l2 = [int(element) for element in l1]

# Returns
l2
[1, 2]                              # Python 2, 3
'<map object at 0x7fde348ff6d8>'    # Python 3 when using map


# Filter -- return elements of a list that satisfy a given condition.

l1 = [0, 1]

# Fine
l2 = []
for element in l1:
    if l1:
        l2.append(element)

# Better.
l2 = filter(bool, l1)

# Better.
l2 = [bool(element) for element in l1]

# Returns
l2
[1]                                 # Python 2, 3
'<filter object at 0x7fde3491ddd8>' # Python 3 when using map


# Reduce -- Apply a function compoundingly to a list.

l = [1, 2, 3]

# Fine
multiplied = 1
for element in l:
    multiplied *= element


# Better
from functools import reduce
from operators import mul


multiplied = reduce(mul, l)

# Returns
multiplied
6



""" Lambda functions (one-time-use functions) """

# E.g.
addone = lambda x: x + 1
addone(1)
2

sum_variables = lambda x, y: x + y
sum_variables(1, 1)
2

# Most commonly used with map, filter, and reduce

l1 = [1, 2]

# Map

l2 = map(lambda x: x**2, l1)

l2
[1, 4]                                      # Python 2
'<map object at 0x000000e000b0>'            # Python 3

# Filter 

l2 = filter(lambda x: x > 1, l1)

l2
[2]                                         # Python 2
'<filter object at 0x000000e000b0>'         # Python 3

# Reduce

l2 = reduce(lambda x1, x2: x1 * x2, l1)

l2
2




"""
The next section is a summary of the code in Raymond Hettinger's

"Transforming Code into Beautiful, Idiomatic Python"

https://www.youtube.com/watch?v=OSGv2VnC0go

"""



""" Looping over a range of numbers """

# Use range.

for i in [1, 2, 3, 4, 5]:
    print(i**2)


# Best for Python 3.

for i in range(6):
    print(i**2)


# Best for Python 2.

for i in xrange(6):
    print(i**2)
    


""" Looping over a collection. """

colors = ['red', 'green', 'blue', 'yellow']


# Looping through items.

# Bad.
for i in range(len(colors)):
    print(colors[i])

# Good.
for color in colors:
    print(color)    


""" Looping backwards through items. """


# Bad.
for i in range(len(colors) - 1, -1, -1):
    print(colors[i])


# Good.
for color in reversed(colors):
    print(color)


""" Looping through a collection with indices. """

# Bad.
for i in range(len(colors)):
    print(i, colors[i])


# Good.
for i, color in enumerate(colors):
    print(i, color)


""" Looping over two collections """

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']


# Bad.
n = min(len(names), len(colors))
for i in range(n):
    print(names[i], colors[i])


# Good for Python 3.
for name, color in zip(names, colors):
    print(name, color)


# Good for Python 2. 
for name, color in izip(names, colors):
    print(name, color)


""" Custom Sort Order """

colors = ['red', 'green', 'blue', 'yellow']

def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0

def sorter(val):
    return val[1]

from operator import itemgetter

print( sorted(colors, cmp=compare_length) )
print( sorted(colors, key=itemgetter(1)) )
print( sorted(colors, key=len, reversed=True) )


""" Distinguishing multiple exit points in loops. """

# Bad.
def find(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i


# Good.
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i


""" Looping over dictionary keys """

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

for key in d:
    print(key, d[key])

# Python 3.
for key, value in d.items():
    print(key, value)

# Python 2.
for key, value in d.iteritems():
    print(key, value)

# Creates a copy of keys so you can mutate the dict.
for key in d.keys():
    if key.startswith('r'):
        del(d[key])

# Dictionary comprehension.

d = {k : d[k] for k in d if not k.startswith('r')}

l = [i for i in range(3) if i > 1]
l = [i if i > 1 else 0 for i in range(3)]

# Creating dictionaries with lists.

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']


# Python 3.
d = dict(zip(names, colors))

# Python 2.
from itertools import izip
d = dict(izip(names, colors))


""" Counting with dictionaries. """

colors = ['red', 'green', 'red', 'blue', 'green', 'red']


d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1

{'blue': 1, 'green': 2, 'red': 3}

d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1

# With default dictionary
from collections import defaultdict

d = defaultdict(int)
for color in colors:
    d[color] += 1


# With Counter
from collections import Counter

n_colors = Counter(colors) 


""" Grouping with dictionaries"""

names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']


# Fine

d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)

{5: ['roger', 'betty'], 6: ['rachel', 'judith'], 
 7: ['raymond', 'matthew', 'melissa', 'charlie']}


# Better

d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)

# Best

from collections import defaultdict

d = defaultdict(list)
for name in names:
        key = len(name)
        d[key].append(name)



# Contribute to your companies code base by adding docstrings. 
# People will love you for it and you'll learn the codebase.


""" Thread-safe dictionary use. """

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

while d:
    key, value = d.popitem()
    print(key, value)



""" Linking Dictionaries """


# Default command line arguments.

# Fine.

import os
import argparse

defaults = {'color': 'red', 'user': 'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args([])
command_line_args = {k:v for k, v in vars(namespace.items()) if v}

d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)

# Better and faster.

from collections import ChainMap

d = ChainMap(command, os.environ, defaults)

# E.g. 1 
d1 = {'a': 1, 'b': 2}
d2 = {'a': 3}
d3 = {'a': 4, 'b': 3}

ChainMap(d1, d2, d3)

{'b': 2, 'a': 1}


# E.g. 2 
d1 = {}
d2 = {'a': 3}
d3 = {'a': 4, 'b': 3}

ChainMap(d1, d2, d3)

{'b': 3, 'a': 3}


""" Improving clarity. """


# Clarifying function calls with keyword arguments.

twitter_search('@obama', False, 20, True)

twitter_search('@obama', retweets=False, numtweets=20, popular=True)


# Named tuples.

doctest.testmod()
(0, 4)


doctest.testmod()
TestResults(failed=0, attempted=4)

from collections import namedtuple

TestResults = namedtuple('TestResults', ['failed', 'atttempted'])

# Unpacking sequences

p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'

fname = p[0]
lname = p[1]
age   = p[2]
email = p[3]

fname, lname, age, email = p

# Updating multiple state variables

def fibonaci(n):
    x = 0
    y = 1
    for i in range(n):
        t = y
        y = x + y
        x = t


def fibonaci(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y

# Simultaneous state updates.

def influence(m, x, y, dx, dy, partial):
    pass

# Bad
tmp_x = x + dx * t
tmp_y = y + dy * t
tmp_dx = influence(m, x, y, dx, partial='x')
tmp_dy = influence(m, x, y, dy, partial='y')
x = tmp_x
y = tmp_y
dx = tmp_dx
dy = tmp_dy

# Good
x, y, dx, dy = (x + dx * t,
                y + dy * t,
                influence(m, x, y, dx, partial='x'),
                influence(m, x, y, dy, partial='y'))


# Concatenating strings.

# Bad (quadratic)
s = name[0]
for name in names[1:]:
    s += ', ' + name
print(s)


# Good
s = ', '.join(names)
print(s)


# Updating Sequences

names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

# Bad
del a[0]
names.pop(0)
names.insert(0, 'mark')

from collections import deque

names = deque(names)

del names[0]
names.popleft()
names.appendleft('mark')
