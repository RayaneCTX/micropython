# test the special functions imported from math

try:
    from math import *

    erf
except (ImportError, NameError):
    print("SKIP")
    raise SystemExit

test_values = [
    -8.0,
    -2.5,
    -1,
    -0.5,
    0.0,
    0.5,
    2.5,
    8.0,
]
pos_test_values = [
    0.001,
    0.1,
    0.5,
    1.0,
    1.5,
    10.0,
]

functions = [
    ("expm1", expm1, test_values),
    ("log2", log2, test_values),
    ("log10", log10, test_values),
    ("cosh", cosh, test_values),
    ("sinh", sinh, test_values),
    ("tanh", tanh, [-1e6, -100] + test_values + [100, 1e6]),
    ("acosh", acosh, [1.0, 5.0, 1.0]),
    ("asinh", asinh, test_values),
    ("atanh", atanh, [-0.99, -0.5, 0.0, 0.5, 0.99]),
    ("erf", erf, test_values),
    ("erfc", erfc, test_values),
    ("gamma", gamma, pos_test_values),
    ("lgamma", lgamma, pos_test_values + [50.0, 100.0]),
]

for function_name, function, test_vals in functions:
    print(function_name)
    for value in test_vals:
        try:
            print("{:.4g}".format(function(value)))
        except ValueError as e:
            print(str(e))

functions_var_args = [
    (
        "gcd",
        gcd,
        (
            (1, 4),
            (2, 8),
            (0, 8),
            (-1, 19),
            (-5, 42),
            (-7, -7),
            (-9, -2),
            (0, 0),
            (6, 30, 40, -60, 20, 40),
            (2147483643, 42),
            (-2147483647, -214748364, 21474836),
        ),
    ),
]

for function_name, function, test_vals in functions_var_args:
    print(function_name)
    for values in test_vals:
        try:
            print("{:.4g}".format(function(*values)))
        except ValueError as e:
            print(str(e))

print(gcd(12345678912345678912345678911561561658135153135135135, 123456))

lcm_function_args = [
    (
        "lcm",
        lcm,
        (
            (1, 4),
            (2, 8),
            (0, 8),
            (-1, 19),
            (-5, 42),
            (-7, -7),
            (-9, -2),
            (0, 0),
            (6, 30, 40, -60, 20, 40),
            (2147483643, 42),
            (-2147483647, -214748364, 21474836),
        ),
    ),
]

for function_name, function, test_vals in functions_var_args:
    print(function_name)
    for values in test_vals:
        try:
            print("{:.4g}".format(function(*values)))
        except ValueError as e:
            print(str(e))
