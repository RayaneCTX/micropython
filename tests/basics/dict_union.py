# Tests for dictionary union.
# Using sorted() for now until map insertion order is implemented within
# micropython.

d = {'spam': 1, 'eggs': 2, 'cheese': 3}
e = {'cheese': 'cheddar', 'aardvark': 'Ethel'}
print(sorted(d | e))
print(sorted(e | d))
d |= e
print(sorted(d))
