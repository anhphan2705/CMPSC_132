def foo(num):
    return 2 * bar(num)
    
def bar(num):
    num = x + 1
    return num
    
num = 2 
x = 3
print(foo(bar(x)))
print(num, x)