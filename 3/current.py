#   №10

p = []
for n in range(1, 1000):
    n = bin(n)[2:]
    n += str(int(n.count('1'))%2)
    n += str(int(n.count('1')) % 2)
    r = int(n, 2)
    if r > 97:
        p.append(r)
print(min(p))


