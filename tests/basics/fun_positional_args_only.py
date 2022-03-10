# def foo(x, y = 2, /):
#     print("foo")
def f(pos1, pos2, *, pos_or_kwd, /, kwd1, kwd2):
    pass

f(1, pos2=1, pos_or_kwd=2, kwd2=2, kwd1=1)

#
# f(1, 2, 3, kwd1=4, kwd2=5)
# def bar(x, y):
#     print("bar")

# print("g")
# foo(1, 2)
# print("g")
# bar(1,2)
