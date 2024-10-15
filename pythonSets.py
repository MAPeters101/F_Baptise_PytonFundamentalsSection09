s = {'a', 'b', 'c'}
print(type(s))

s = set(['a','b','c'])
print(type(s), s)

s = set('abc')
print(type(s), s)

s = set('python')
print(type(s), s)

s = set(['a', 'a', 'b', 'b'])
print(type(s), s)

s = set('banana')
print(type(s), s)

s = {}
print(type(s), s)

s = set()
print(type(s), s, len(s))

s = set('python')
print(s)
print('p' in s, 'x' not in s)

for item in s:
    print(item)

s2 = s.copy()
print(s2)

from copy import deepcopy
s2 = deepcopy(s)

print(s2)
