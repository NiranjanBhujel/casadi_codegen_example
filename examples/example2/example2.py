# Create mapping f1=[x1**2 + x2 * y1 + x3, x1**2], f2 = x2 * y2

import casadi as ca

# Variables
x = ca.SX.sym("x", 3)
y = ca.SX.sym("y", 2)

x1 = x[0]
x2 = x[1]
x3 = x[2]

y1 = y[0]
y2 = y[1]


f1 = ca.vertcat(x1**2 + x2 * y1 + x3, x1**2)
f2 = x2 * y2

func = ca.Function(
    'func',
    [x, y],  # inputs x and y
    [f1, f2],  # outputs f1 and f2
    ['x', 'y'],  # inputs name
    ['f1', 'f2']  # outputs name
)


func.generate('test_example', {'with_header': True, 'casadi_int': 'int', 'indent': 4})

print(f"arg_size: {func.sz_arg()}")
print(f"res_size: {func.sz_res()}")
print(f"iw_size: {func.sz_iw()}")
print(f"w_size: {func.sz_w()}")