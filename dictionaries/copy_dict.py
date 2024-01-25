d1 = {"a":11, "b":22, "c":33}
d2 = d1.copy()
print ("id:", id(d1), "dict: ",d1)
print ("id:", id(d2), "dict: ",d2)
d1["b"] = 100
print ("id:", id(d1), "dict: ",d1)
print ("id:", id(d2), "dict: ",d2)

# Output:
# d: 1586671734976 dict: {'a': 11, 'b': 22, 'c': 33}
# id: 1586673973632 dict: {'a': 11, 'b': 22, 'c': 33}
# id: 1586671734976 dict: {'a': 11, 'b': 100, 'c': 33}
# id: 1586673973632 dict: {'a': 11, 'b': 22, 'c': 33}