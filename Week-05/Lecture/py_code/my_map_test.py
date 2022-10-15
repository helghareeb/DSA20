# بسم الله الرحمن الرحيم

# from my_map_imp_one import MyMap
from my_map_imp_two import MyMap


m = MyMap()
m.add(0, 'Zero')
m.add(1, 'One')
m.add(2, 'Two')

for i in m:
    print(i, m[i])

print(0 in m)

print(9 in m)

m.add(0, 'ZZZero')
m.add(5, 'Five')
m.add('Seven', 7)

for i in m:
    print(i, m[i])

# m.remove('Seven')

# for i in m:
#     print(i, m[i])


# for a,b in enumerate(m):
#     print(a,b)
