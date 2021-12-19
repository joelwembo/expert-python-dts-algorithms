import sympy as sym

x , y, z = sym.symbols('X Y Z')

exp = x**3 + y + y**3 + z

derivativel_x = sym.diff(exp, x)
print('derivative w.r.t.x: ' , derivativel_x)

# Differentiating exp with respect to y

derivativel_y = sym.diff(exp, y)
print('derivative w.r.t y: ' , derivativel_y)

# Calcutlating limit of f(x) = x as x->∞

limit1 = sym.limit(x, x, sym.oo)
print(limit1)
 
# Calculating limit of f(x) = 1/x as x->∞
limit2 = sym.limit(1/x, x, sym.oo)
print(limit2)
 
# Calculating limit of f(x) = sin(x)/x as x->0
limit3 = sym.limit(sym.sin(x)/x, x, 0)
print(limit3)



