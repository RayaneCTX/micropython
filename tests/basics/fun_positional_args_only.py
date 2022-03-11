# def foo(x, y = 2, /):
#     print("foo")
def f(pos1, pos2=1, /, pos3=3, *, kwd1, kwd2=3):
    pass

f(1, kwd2=2, kwd1=1)

#
# f(1, 2, 3, kwd1=4, kwd2=5)
# def bar(x, y):
#     print("bar")

# print("g")
# foo(1, 2)
# print("g")
# bar(1,2)
