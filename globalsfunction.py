a = 10
print(id(a))
def var():
    a = 9
    x = globals()['a']
    print(id(x))
    print("value of x after global veriable",x)
    print("local is",a)
    globals()['a'] = 15
var()
print("global is",a)