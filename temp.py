from sympy import symbols, groebner
o, x, y, z, a, b, c, d = symbols('o x y z a b c d')

f1 = -x + a + b - a*b
f2 = -y + b + c - 2*b*c
f3 = -z + (1-c)*d
f4 = -o + x*y*z

ideal = [f1, f2, f3, f4]

G = groebner(ideal, o, x, y, z, a, b, c, d)

for g in G:
    print(g)
