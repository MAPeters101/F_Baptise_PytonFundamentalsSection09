s1 = set('abc')
s2 = {True, False}
s3 = {'a', 100, 200}

print(s1.isdisjoint(s2))
print(s2.isdisjoint(s1))
print(s1.isdisjoint(s3))
s = set()
s.add(100)
print(s)
s.add(200)
print(s)
s.add(200)
print(s)
s = set('abc')
print(s)
s.remove('a')
print(s)
s.discard('b')
print(s)
s.discard('x')
print(s)
#s.remove('x')
print(s)
print('+'*20)

s1 = set('abc')
s2 = set('abcd')
print(s1 < s2)
print(s1 <= s2)
print(s2 >= s1)
print(s2 > s1)
s1 = set('abc')
print(s1 < s3)
print(s1 <= s3)
print('+'*20)

s1 = set('abc')
s2 = set('bcd')

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s2 - s1)

