#    №12

def per(a, b):
    x = ''
    while a >= b:
        x += str(a%b)
        a //= b
    x += str(a)
    return x[::-1]


p = []
for n in range(1, 1000):
    r = per(n, 3)
    r += str(n%3)
    r = int(r, 3)
    if r > 999:
        p.append(r)
print(min(p))