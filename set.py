#Sets

Sets.py

include a data type for sets.
Curly branes or the set() function can be used to create set.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)           # show that duplicates have been removed

'orange' in basket              # fast membership testing
'crabgrass' in basket


Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                 # unique letters in a
a - b                             # letters in a but not in b
a | b                             # letters in a or b or both
a & b                             # letters in both a and b
a ^ b                             # letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
a

--------

>>> x = set('23802348')
>>> y = set('57839012')
>>> x - y
{'4'}
>>> y - x
{'9', '5', '7', '1'}
>>> x ^ y
{'9', '5', '7', '4', '1'}
>>> y | x
{'9', '5', '8', '0', '2', '3', '7', '4', '1'}
>>> x = set('23802348')
>>> y = set('57839012')
>>> x -y
{'4'}
>>> y -x
{'9', '5', '7', '1'}
>>> x ^ y
{'9', '5', '7', '4', '1'}
>>> y | x
{'9', '5', '8', '0', '2', '3', '7', '4', '1'}
>>> x & y
{'0', '8', '2', '3'}

>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'d', 'r'}
>>> a = {x for x in 'abracadabra' if x in 'abc'}
>>> a
{'b', 'c', 'a'}

fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)

When looping through dictionaries 

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
        print(k, v)