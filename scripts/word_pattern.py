'''
Given an array strings, determine whether it follows the sequence given in the patterns array. In other words,
there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j]
or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

Example

For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = true;
For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = false.
'''

# default dict simplifies the situations where we want to check a key in a dictionary
# that might not have been given a value yet. However, this introduces a bug if your patterns array has
# the default value.
from collections import defaultdict
def areFollowingPatterns(strings, patterns):
	# if the lengths are different, then then strings cannot possibly follow the pattern.
    if len(strings) != len(patterns):
        return False
    n = len(strings)
	# make two dictionaries to track word-pattern associations and check
	# whether we have seen a word or pattern before
    word_dict = defaultdict(str) # {word: pattern}
    pattern_dict = defaultdict(str) # {pattern: word}
    for i in range(n):
        word = strings[i]
        pattern = patterns[i]
		# if the word is new and the pattern is new, then we add {word:pattern} to the word dictionary
		# and add {pattern:word} to the pattern dictionary. Note we need both dictionaries because it's possible
		# for a word to be new and not the pattern, and vice versa, so we really need to check that both the word and
		# pattern are new.
        if word not in word_dict and pattern not in pattern_dict:
            word_dict[word] = pattern
            pattern_dict[pattern] = word
		# Otherwise, we have already encounterend this word or pattern before, so the pattern
		# better match what we already have stored. If it doesn't, then we are not following the pattern.
        elif word_dict[word] != pattern or pattern_dict[pattern] != word:
            return False
    return True

strings = ['cat', 'dog', 'doggy']
patterns = ['a','','']
print(areFollowingPatterns(strings,patterns))