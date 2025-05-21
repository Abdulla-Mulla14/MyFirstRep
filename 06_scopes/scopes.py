def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(4)
g = chaicoder(6)

print(f(3))
print(g(3))
