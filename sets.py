# create an empty set
s = set()

# add elements to set

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.add(4) # no element is repeated inside a set.

print(s)

# removing elements from set

s.remove(2)

print(s)

# printing length of elements in the set

print(f"the set has {len(s)} elements.")