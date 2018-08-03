##import random
##import queue
##
##q = queue.Queue()
##
##randlist = list(range(1,11))
##print(randlist)
##random.shuffle(randlist)
##print(randlist)
##
##for i in randlist:
##    q.put(i)
##
##if not q.empty():
##    print("hihihihihih")
##

##import itertools
##
##permlist = [i for i in range(1,4)]
##print(permlist)
##
##x = itertools.permutations(permlist,len(permlist))
##xlist = list(x)
##
##print(xlist)
##
##print(xlist[0][2])

x = "sup bro"
print('I love the number %s' %x)
