"""Count words."""

def getKey0(item):
    return item[0]
def getKey1(item):
    return item[1]

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    sList = s.split() # this makes a list of words in the original string
    countList = [ sList.count(i) for i in sList ] # list of counts of entries in sList
    sTuple = [ [i , sList.count(i) ] for i in sList ]
    # list of lists with words as 0th index and their counts as 1st index
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    sTuple = sorted(sTuple, key = getKey1, reverse = True)
    for i in range(0,len(sTuple)):
        for j in range(0,len(sTuple)):
            if sTuple[i][1] == sTuple[j][1] and sTuple[i][0] < sTuple[j][0]:
                sTuple[i][0], sTuple[j][0] = sTuple[j][0] , sTuple[i][0]
    
    top_n = []
    
    while len(sTuple) > 0 and len(top_n) < n:
        top_n.append( (sTuple[0][0],sTuple[0][1]) )
        repeat = sTuple[0]
        while repeat in sTuple:
            sTuple.remove(repeat)
    
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print( count_words("cat bat mat cat bat cat", 3) )
    print( count_words("betty bought a bit of butter but the butter was bitter", 3) )


if __name__ == '__main__':
    test_run()


