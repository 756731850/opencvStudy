def trim(s):
    for i in range(len(s)):
        if s[:1] == ' ':
            s = s[1:]
        if s[-1:] == ' ':
            s = s[:-2]
    return s


#yield 生成器
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a, b  =  b,a + b
        n = n+1
    return "done"

k = fib(5)
print(next(k))
print(next(k))
print(next(k))
print(next(k))

def yanghui(n):
    l = [1]
    while True:
        yield l
        l = [1] + [l[x] + l[x + 1] for x in range(len(l) - 1)] + [1]
        if len(l) > n:
            break

m = yanghui(6)
for i in m:
    print(i)


#迭代器iterable
#凡是可作用于for循环的对象都是Iterable类型；

#凡是可作用于next()函数的对象都是Iterator类型
# ，它们表示一个惰性计算的序列；

#集合数据类型如list、dict、str等是Iterable但不
# 是Iterator，不过可以通过iter()函数获得一个Iterator对象。

# functools.partial就是帮助我们创建一个偏函数的，


#map和reduce
def f(x):
    return x * x

r = map(f, [1,2,3])
list(r)
print(r)
print(list(r))

from functools import reduce
def fn(x, y):
    return x * 10 + y

#关键字lambda表示匿名函数，冒号前面的x表示函数参数。 例如：lambda x: x * x

#装饰器由于函数也是一个对象，而且函数对
# 象可以被赋值给变量，所以，通过变量也能调用该函数。
#>>> def now():
#...     print('2015-3-25')
#...
#>>> f = now
#>>> f()

print(reduce(fn, [1, 3, 5, 7, 9]))

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

str = '  h e l lo tony '
x = trim(str)
print(x)


