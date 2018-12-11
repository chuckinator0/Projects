'''
One summer Felicia was visiting her granny's summer house. There were several old and withered vines growing in the garden, that no longer produced grapes.
Felicia found it sad, and decided to decorate the vines with wooden grapes she carved out herself. She also watered them with cola, since cola makes everything better.

When winter came, Felicia left, but the vines were still there, better than ever before. Each year they grew higher and wider, and the pairs of neighboring vines
entangled together, forming a single vine. The wooden grapes were also doing just fine: they remained firmly attached to the vines.

Now that n years has passed, Felicia is going to visit her granny again, and she is curious about how the vines are doing. Given the number of grapes she hang on the vines,
return the number of grapes on each vine after n years, assuming that each year the (2 * i - 1)th and the (2 * i)th vines (1-based) merged into a single vine
(for each integer i in range [1, <number_of_vines> / 2]).

Example

For vines = [1, 2, 3, 4, 5] and n = 2, the output should be
mergingVines(vines, n) = [10, 5].

After the first year vines two pairs of vines entangled: vines 1 and 2 and vines 3 and 4 (1-based). The last vine didn't have anything to entangle with.
The vines could thus be represented as [3, 7, 5].
After the second year, another pair of vines entangled. The first and the second vines entangled, forming a single vine. It's possible to represent the vines as [10, 5],
which is the answer.
'''

# This one is very complicated and taught me some stuff about decorators that I'm still processing.
# (I'm sure there's more straightforward solutions, but this particular exercise taught me a lot about decorators specifically.)
# Basically, we use a decorator when we want to modify a function "from the outside". By that,
# I mean we don't actually want to change the code of the function itself, in case it's used elsewhere in the way originally intended.
# To do this modification, we write a new function that takes a function as input and outputs a slightly different function. We then use
# a !!!!!decorator!!!!! (yay!!) above the original function that tells Python that the function is slightly modified here.

# This problem goes a little step further and includes an argument that affects how the function will be modified. You'll see.

from functools import reduce


def mergingVines(vines, n):

	# We will use this function to modify the sumOnce function further down.
	# nTimes is itself a function object. When we use it as a decorator, an
	# input of sumOnce (another function object) will be passed into it.
	def nTimes(func):
		# We want to return a function, so we define a wrapper function that modifies
		# the behavior of func to what we want. Here, we want func to compose with itself n times.
		def wrapper(*args,**kwargs):
			# if the function has been applied 0 times, its effect is that of the identity function
			if n == 0:
				return (lambda x: x)(*args,**kwargs)
			else:
				return reduce(lambda f,g: lambda x: f(g(x)) , [ func for _ in range(n) ])(*args,**kwargs)
		# we return this wrapper function object, so when nTimes decorates sumOnce,
		# the sumOnce function will be passed as an argument to nTimes. Note that we could have
		# just passed the vines variable into wrapper, but in general, decorators might decorate functions
		# with different numbers or kinds of inputs, so we can use *args (lists of arguments) and
		# **kwargs (keyword arguments) to be more general.
		return wrapper
			

	# Here's the decorator! We are modifying the sumOnce function
	@nTimes
	def sumOnce(vines):
		res = [vines[i] + vines[i + 1] for i in range(0, len(vines) - 1, 2)]
		if len(vines) % 2 == 1:
			res.append(vines[-1])
		return res

	# The decorator has modified sumOnce, so now when we call it, it will actually be applied n times, as
	# specified by the decorator function.
	return sumOnce(vines)




print(mergingVines([1,2,3,4,5],2))