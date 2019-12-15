def build_quadratic_function(a, b, c):
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(3, 0, 1)(2)
print(f)
