def foo(x, y, /):
    print("f")

def bar(x, y):
    print("bar")

print("g")
foo(x=1,y=2)
print("g")
bar(1,2)
