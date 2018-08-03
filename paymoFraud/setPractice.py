##dictionary = {}
##
##for i in range(5):
##    dictionary[i] = set()
##
##dictionary[3].add(6)
##dictionary[3].add(15)
##dictionary[3].add(6)
##print(dictionary)
##
##for element in dictionary[3]:
##    print(element*element)


d = {42: True, 420: False, 4200: True}
d[42000] = True
if d[420] == False:
    print('hi')
