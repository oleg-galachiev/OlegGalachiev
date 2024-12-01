#    №15



import itertools

z = 0
p=[]
sim = 'ИВАН'
ar = itertools.product(sim, repeat = 5 )
for i in ar:
    p.append(list(i))
for k in p:
    if k.count("И") >= 1:
        z += 1
print(z)