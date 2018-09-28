"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

def minWordLength(wordList):
    """Calculate the shortest length of the words in the list. The reason
    we want to do this is because we want to limit the index in the longestCommonPrefix function"""
    minLength = len(wordList[0])
    for word in wordList:
        if len(word) < minLength:
            minLength = len(word)
    return minLength

def lettersMatch(index, wordList):
    letter = wordList[0][index]
    for word in wordList:
        if letter != word[index]:
            return False
    return True

# def longestCommonPrefix(wordList):
#     if wordList == []:
#         return ''
#     minWordLen = minWordLength(wordList)
#     prefix = ''
#     for index in range(minWordLen):
#         if lettersMatch(index,wordList):
#             prefix += wordList[0][index]
#         else:
#             return prefix
#     return prefix

# More efficient with while loop with error handling!
def longestCommonPrefix(wordList):
    if wordList == []:
        return ''
    prefix = ''
    index = 0
    while True:
        try:
            if lettersMatch(index,wordList):
                prefix += wordList[0][index]
                index += 1
            else:
                return prefix
        except IndexError:
            return prefix

            


print(longestCommonPrefix(['food','foooooooooooo','fool']))
