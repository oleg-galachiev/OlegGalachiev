#   №13


import itertools

z = 0
p=[]
sim = 'ABCX'
ar = itertools.product(sim, repeat = 5 )
for i in ar:
    p.append(list(i))
for k in p:
    if k.count('X') == 1 and (k[0] == 'X' or k[-1] == 'X'):
        z += 1
print(z)
