'''
Sort dictionaries by value in dictionaries in a pretty way
'''

dic = { 'a':5,
		'b': 2,
		'c': 4
		}

# Good, but ugly. dic.items() gives us a list of tupes (key,value).
# We access the tuple at index 1 to get the value. Our sort key is the value.
# lambda extracts a single element of the object to be sorted.
y = sorted(dic.items(), key = lambda tup: tup[1])
print(y)

# better, I think. This will output just the keys after sorting.
# our lamda element is a key in dic, and dic.get(k) says we are sorting by
# value.
z = sorted(dic, key = lambda k: dic.get(k))
print(z)

# Build on last idea to display same as before
w = [(key,dic[key]) for key in z]
print(w)

