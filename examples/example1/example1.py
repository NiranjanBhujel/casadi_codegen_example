import casadi as ca

# Variables
x = ca.SX.sym("x")
y = ca.SX.sym("y")

# Parameters to be provided in runtime
a = ca.SX.sym("a")

J = x**2 + (y-1)**2

optim_prob = {
    "x": ca.vertcat(x, y),
    "f": J,
    "g": x + y - a,
    "p": a
}

S = ca.nlpsol("S", "sqpmethod", optim_prob, {"qpsol": "qrqp"})

# input argument
a_in = ca.MX.sym("a_in")
r = S(lbg=0, ubg=ca.inf, p=a_in)
x_opt = r["x"]


solver_func = ca.Function(
    "solver_func",
    [a_in],
    [x_opt[0], x_opt[1]],
    ["a"],
    ["x", "y"]
)

solver_func.generate(
    "test.c",
    {
        'main': False,
        'mex': False,
        'with_header': True
    }
)

print(f"arg_size: {solver_func.sz_arg()}")
print(f"arg_size: {solver_func.sz_res()}")
print(f"arg_size: {solver_func.sz_iw()}")
print(f"arg_size: {solver_func.sz_w()}")
