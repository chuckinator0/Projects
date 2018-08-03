"""
This program defines a function that counts the number of valid rhyme schemes with 'k' lines.
Each line of the poem is assigned a letter so that all lines with the same letter rhyme with one another.
The first time that a letter is used in a rhyme scheme, it must be the earliest letter in the alphabet yet to be used.
Valid rhyme schemes: AABB, ABCB, AAAB.
Invalid rhyme schemes: AAAC, ABDC, ABDB.
For convenience, instead of letters A,B,C, etc., this program will label with 0,1,2,3, etc.
"""


def newTuple(schemeTuple):
    """This function takes a list of tuples of rhyme schemes of poems with 'k' lines and appends the next 'letter' when
    it doesn't violate the rules of valid rhyme schemes. The output is a new list of schemes of length 'k+1'."""
    k = len(schemeTuple[0])
    'k is the number of lines in the poem'
    newTuple = []
    for i in range(k+1):
        for scheme in schemeTuple:
            if (i in scheme) or (i-1 in scheme):
                newScheme = list(scheme)
                newScheme.append(i)
                newTuple.append(tuple(newScheme))
    return newTuple

def schemes(n):
    """This function outputs a list of all possible rhyme schemes for poems with 'n' lines."""
    if n < 0:
        raise ValueError("Please input a non-negative integer")
    elif n == 0:
        return [tuple()]
    elif n == 1:
        return [tuple([0])]
    else:
        return newTuple(schemes(n-1))


for i in range(6):
    print(len(schemes(i)))