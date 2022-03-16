# positional_args_only tests

# Tests sourced from 
# https://github.com/python/cpython/blob/main/Lib/test/test_positional_only_arg.py

def tryFunctionFail(s):
    try:
        eval(s)
        print("FAILED: %s did not throw syntax error." % repr(s))
    except Exception as e:
        print("PASSED: %s threw '%s'" % (repr(s), e))

def tryFunctionPass(s):
    try:
        eval(s)
        print("PASSED: %s did not throw syntax error." % repr(s))
    except Exception as e:
        print("FAILED: %s incorrectly threw syntax error." % repr(s))

##################################################
# test_invalid_syntax_errors 
# test_invalid_syntax_errors_async
invalid_tests = [
    "def f(a, b = 5, /, c): pass",
    "def f(a = 5, b, /, c): pass",
    "def f(a = 5, b=1, /, c, *, d=2): pass",
    "def f(a = 5, b, /): pass",
    "def f(*args, /): pass",
    "def f(*args, a, /): pass",
    "def f(**kwargs, /): pass",
    "def f(/, a = 1): pass",
    "def f(/, a): pass",
    "def f(/): pass",
    "def f(*, a, /): pass",
    "def f(*, /, a): pass",
    "def f(a, /, a): pass",
    "def f(a, /, *, a): pass",
    "def f(a, b/2, c): pass",
    "def f(a, /, c, /): pass",
    "def f(a, /, c, /, d): pass",
    "def f(a, /, c, /, d, *, e): pass",
    "def f(a, *, c, /, d, e): pass",
    "async def f(a, b = 5, /, c): pass",
    "async def f(a = 5, b, /, c): pass",
    "async def f(a = 5, b=1, /, c, d=2): pass",
    "async def f(a = 5, b, /): pass",
    "async def f(*args, /): pass",
    "async def f(*args, a, /): pass",
    "async def f(**kwargs, /): pass",
    "async def f(/, a = 1): pass",
    "async def f(/, a): pass",
    "async def f(/): pass",
    "async def f(*, a, /): pass",
    "async def f(*, /, a): pass",
    "async def f(a, /, a): pass",
    "async def f(a, /, *, a): pass",
    "async def f(a, b/2, c): pass",
    "async def f(a, /, c, /): pass",
    "async def f(a, /, c, /, d): pass",
    "async def f(a, /, c, /, d, *, e): pass",
    "async def f(a, *, c, /, d, e): pass"
]
for s in invalid_tests:
    tryFunctionFail(s)

##################################################
# test_optional_positional_only_args
print("\ntest_optional_positional_only_args")
def assertEqual(f, res):
    assert(f == res)

def f(a, b=10, /, c=100):
    return a + b + c

assertEqual(f(1, 2, 3), 6)
assertEqual(f(1, 2, c=3), 6)
tryFunctionFail("f(1, b=2, c=3)")

assertEqual(f(1, 2), 103)
tryFunctionFail("f(1, b=2)")
assertEqual(f(1, c=2), 13)

def f(a=1, b=10, /, c=100):
    return a + b + c

assertEqual(f(1, 2, 3), 6)
assertEqual(f(1, 2, c=3), 6)
tryFunctionFail("f(1, b=2, c=3)")

assertEqual(f(1, 2), 103)
tryFunctionFail("f(1, b=2)")
assertEqual(f(1, c=2), 13)

##################################################
# test_syntax_for_many_positional_only
print("\ntest_syntax_for_many_positional_only")
tryFunctionPass("def f(%s, /):\n  pass\n" % ', '.join('i%d' % i for i in range(300)))

##################################################
# test_pos_only_definition
print("\ntest_pos_only_definition")
def f(a, b, c, /, d, e=1, *, f, g=2):
    pass

try:
    assertEqual(5, f.__code__.co_argcount)  # 3 posonly + 2 "standard args"
    assertEqual(3, f.__code__.co_posonlyargcount)
    assertEqual((1,), f.__defaults__)

    def f(a, b, c=1, /, d=2, e=3, *, f, g=4):
        pass

    assertEqual(5, f.__code__.co_argcount)  # 3 posonly + 2 "standard args"
    assertEqual(3, f.__code__.co_posonlyargcount)
    assertEqual((1, 2, 3), f.__defaults__)
except Exception as e:
    print("FAILED: test_pos_only_definition")
    print(e)

##################################################
# test_pos_only_call_via_unpacking
print("\ntest_pos_only_call_via_unpacking")
def f(a, b, /):
    return a + b
assertEqual(f(*[1, 2]), 3)

##################################################
# test_use_positional_as_keyword
print("\ntest_use_positional_as_keyword")
def f(a, /):
    pass
expected = r"f() got some positional-only arguments passed as keyword arguments: 'a'"
tryFunctionFail("f(a=1)")

def f(a, /, b):
    pass
expected = r"f() got some positional-only arguments passed as keyword arguments: 'a'"
tryFunctionFail("f(a=1, b=2)")

def f(a, b, /):
    pass
expected = r"f() got some positional-only arguments passed as keyword arguments: 'a, b'"
tryFunctionFail("f(a=1, b=2)")

##################################################
# test_positional_only_and_arg_invalid_calls
print("\ntest_positional_only_and_arg_invalid_calls")

def f(a, b, /, c):
    pass
# r"f() missing 1 required positional argument: 'c'"
tryFunctionFail("f(1, 2)")
# r"f() missing 2 required positional arguments: 'b' and 'c'"
tryFunctionFail("f(1)")
# r"f() missing 3 required positional arguments: 'a', 'b', and 'c'"
tryFunctionFail("f()")
# r"f() takes 3 positional arguments but 4 were given"
tryFunctionFail("f(1, 2, 3, 4)")

##################################################
# test_positional_only_and_optional_arg_invalid_calls
print("\ntest_positional_only_and_optional_arg_invalid_calls")
def f(a, b, /, c=3):
    pass
tryFunctionPass("f(1, 2)")
# "f() missing 1 required positional argument: 'b'"
tryFunctionFail("f(1)")
# "f() missing 2 required positional arguments: 'a' and 'b'"
tryFunctionFail("f()")
# "f() takes from 2 to 3 positional arguments but 4 were given"
tryFunctionFail("f(1, 2, 3, 4)")

##################################################
# test_positional_only_and_kwonlyargs_invalid_calls
def f(a, b, /, c, *, d, e):
    pass
tryFunctionPass("f(1, 2, 3, d=1, e=2)")
# r"missing 1 required keyword-only argument: 'd'"
tryFunctionFail("f(1, 2, 3, e=2)")
# r"missing 2 required keyword-only arguments: 'd' and 'e'"
tryFunctionFail("f(1, 2, 3)")
# r"f() missing 1 required positional argument: 'c'"
tryFunctionFail("f(1, 2)")
# r"f() missing 2 required positional arguments: 'b' and 'c'"
tryFunctionFail("f(1)")
# r" missing 3 required positional arguments: 'a', 'b', and 'c'"
tryFunctionFail("f()")
# r"f() takes 3 positional arguments but 6 positional arguments \(and 2 keyword-only arguments\) were given"
tryFunctionFail("f(1, 2, 3, 4, 5, 6, d=7, e=8)")
# r"f() got an unexpected keyword argument 'f'"
tryFunctionFail("f(1, 2, 3, d=1, e=4, f=56)")

##################################################
# test_positional_only_invalid_calls
def f(a, b, /):
    pass
tryFunctionPass("f(1, 2)")
# f() missing 1 required positional argument: 'b'"
tryFunctionFail("f(1)")
# f() missing 2 required positional arguments: 'a' and 'b'"
tryFunctionFail("f()")
# f() takes 2 positional arguments but 3 were given"
tryFunctionFail("f(1, 2, 3)")

##################################################
# test_positional_only_with_optional_invalid_calls
def f(a, b=2, /):
    pass
tryFunctionPass("f(1)")
# "f() missing 1 required positional argument: 'a'"
tryFunctionFail("f()")
# "f() takes from 1 to 2 positional arguments but 3 were given"
tryFunctionFail("f(1, 2, 3)")

##################################################
# test_no_standard_args_usage
print("\ntest_no_standard_args_usage")
def f(a, b, /, *, c):
    pass

tryFunctionPass("f(1, 2, c=3)")
# TypeError
tryFunctionFail("f(1, b=2, c=3)")

##################################################
# test_change_default_pos_only
print("\ntest_change_default_pos_only")
def f(a, b=2, /, c=3):
    return a + b + c

try:
    assertEqual((2,3), f.__defaults__)
except:
    print("FAILED test_change_default_pos_only")

##################################################
# test_lambdas
print("\ntest_lambdas")
try:
    eval("x = lambda a, /, b: a + b")
    assertEqual(x(1,2), 3)
    assertEqual(x(1,b=2), 3)

    eval("x = lambda a, /, b=2: a + b")
    assertEqual(x(1), 3)

    eval("x = lambda a, b, /: a + b")
    assertEqual(x(1, 2), 3)

    eval("x = lambda a, b, /, : a + b")
    assertEqual(x(1, 2), 3)
except:
    print("FAILED: test_lambdas not working")

##################################################
# test_invalid_syntax_lambda
try:
    tryFunctionFail("lambda a, b = 5, /, c: None")
    tryFunctionFail("lambda a = 5, b, /, c: None")
    tryFunctionFail("lambda a = 5, b, /: None")
    tryFunctionFail("lambda *args, /: None")
    tryFunctionFail("lambda *args, a, /: None")
    tryFunctionFail("lambda **kwargs, /: None")
    tryFunctionFail("lambda /, a = 1: None")
    tryFunctionFail("lambda /, a: None")
    tryFunctionFail("lambda /: None")
    tryFunctionFail("lambda *, a, /: None")
    tryFunctionFail("lambda *, /, a: None")
    tryFunctionFail("lambda a, /, a: None")
    tryFunctionFail("lambda a, /, *, a: None")
    tryFunctionFail("lambda a, /, b, /: None")
    tryFunctionFail("lambda a, /, b, /, c: None")
    tryFunctionFail("lambda a, /, b, /, c, *, d: None")
    tryFunctionFail("lambda a, *, b, /, c: None")
except:
    print("FAILED: test_invalid_syntax_lambda not working")

##################################################
# test_posonly_methods
print("\ntest_posonly_methods")
class Example:
    def f(self, a, b, /):
        return a, b

assertEqual(Example().f(1, 2), (1, 2))
assertEqual(Example.f(Example(), 1, 2), (1, 2))
tryFunctionFail("Example.f(1,2)")
# f() got some positional-only arguments passed as keyword arguments: 'b'
tryFunctionFail("Example().f(1, b=2)")
