# Test function call keyword argument syntax

def test_syntax(code):
    try:
        eval(code)
    except SyntaxError:
        print("SyntaxError in '{}'".format(code))

def f(a):
    return a

test_syntax("f((a)=2)")
test_syntax("f(a()=2)")
test_syntax("f(a or b=2)")
