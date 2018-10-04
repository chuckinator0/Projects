'''
Given a dictionary {restaurant: [list of reviews]}, create a search function that returns a list of restaurants that match the search word. Assume
no punctuation after the word. Super simplified.
'''


# search 1 -- search function does some processing
'''
# given a restaurant, build a set of words in all the reviews of the restaurant
def build_word_set(restaurant, reviews):
  word_set = set()
  for review in reviews[restaurant]:
    review_words = review.split(' ')
    for word in review_words:
      word_set.add(word)
  return word_set

# for each restaurant, build a word set and check if the word is in it.
def search(word,reviews):
  matches = []
  for restaurant in reviews:
    word_set = build_word_set(restaurant,reviews)
    if word in word_set:
      matches.append(restaurant)
  return matches
'''

# search 2 -- all preprocessing is done and then the search function just looks up the word in a dictionary

# build a dictionary of the form {word:  [list of restaurants whose reviews contain the word]}
def build_word_dict(reviews):
  word_dict = {}
  # pick a restaurant
  for restaurant in reviews:
    # check each review
    for review in reviews[restaurant]:
      # split each review into a list of words
      review_words = review.split(' ')
      # add all the words to the word dictionary and add this restaurant to the list
      # of restaurants containing the word
      for word in review_words:
        if word in word_dict:
          word_dict[word].append(restaurant)
        else:
          word_dict[word] = [restaurant]
  return word_dict

# build the word dictionary and then check if the word is in it. Return the list of
# restaurants containing the word.
# alternatively, we could just call the build_word_dict function before this point,
# and just have the word_dict as an input here.
def search(word,reviews):
  word_dict = build_word_dict(reviews)
  return word_dict[word]


reviews = {"India Palace" : ["Delicious food", "Noisy ambiance"], 
           "Tasty Korean" : ["Worst meal ever", "OMG Best MEAL EVER!!"], 
           "Picha": ["Authentic flavors", "so good food"]}

word = 'food'
print(search(word,reviews))




