names=["sangeetha","keer","yashu"]
name=iter(names)
print(next(name))
print(next(name))
print(next(name))

def num(x):
    yield x*2
g=num(5)
for i in g:
    print(i)