# reduce() : used to represent the iterable as a single value.
# from functools import reduce # always you need to import for using reduce function
# syntax : reduce(fuction, iterable)

from functools import reduce 
# sum of all values in a list.

amount = [120, 230, 344, 450]
total = reduce(lambda a1, a2 : a1 + a2, amount)
print(total)

# create a list of words and combine as a sentence.

words = ['I', 'am', 'Jitendra', 'Dewangan']
sentence = str(reduce(lambda a1, a2 : a1+' '+a2, words))
print(sentence)
