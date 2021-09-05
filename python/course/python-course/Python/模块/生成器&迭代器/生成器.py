"""
生成器:

    使用了 yield 的函数被称为生成器（generator）。
    跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
    在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。

生成器优点:

    节省内存，不用一次性生成一个完整的list，而是通过next()方法每次推算出下一个内容。

"""
# 创建一个生成器函数
def Generator(sum):

    count = 0
    while count < sum:

        yield count

        count += 1

consumers = Generator(10)

print(next(consumers))
print(next(consumers))
print(next(consumers))
print(next(consumers))
print(next(consumers))
print(next(consumers))
