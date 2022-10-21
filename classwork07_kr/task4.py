def foo(a):
    if a % 2 == 0:
        return False
    if a % 2 != 0:
        return True

itog = filter(foo, generator)
print(itog)