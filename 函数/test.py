
def test():
    g = 6
    # global g
    g = g*2
    print("函数内的值:",g)

g = 5
test()
print("函数外的值:",g)

