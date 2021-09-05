"""
集合: set()

    特性:
        自动去重
        无序类型
        键值必须可以hash
        不可以进行分片
        可以被for循环
        可新增元素
    支持模式:

        交集:    取出大家共存的元素信息
        并集:    去除相同元素信息
        差集:    相对元素确实的部分

    关键字与符号:

        intersection()  交集      &
        union()         并集      |
        difference()    差集      -
        symmetric_difference()  对称差集    ^=


"""
Linux = set(["张三", "李四", "王五", "赵六"])
Python = set(["张三", "李四", "王五", "小白"])


""" 取出Linux 与 Python 都学习的人员信息"""
print(type(Linux))
print(Linux.intersection(Python))
print(Linux&Python)
""" 取出学习所有课程的学员姓名"""
print(Linux.union(Python))
print(Linux|Python)

""" 取出linux班没有学习python的学员信息"""
print(Linux.difference(Python))
print(Linux-Python)

""" 取出python班没有学习linux的学员信息"""
print(Python.difference(Linux))
print(Python-Linux)

""" 取出俩门课程中只单独报名了一门课程的学员信息"""
print(Linux.symmetric_difference(Python))
print(Linux^Python)

""" 内置方法"""
# 删除元素
Linux.remove("张三")
print(Linux)

# 新增元素， 新增元素会被循环加入
Linux.update("客服","1111","22222")  #   {'赵六', '客', '服', '李四', '王五'}
print(Linux)
# 新增一个完整元素
Linux.add("2222")

print(Linux)
# 随机删除元素 删除元素会被记录
info = Linux.pop()
print(Linux)
print(info)

# 从Linux 集合中删除所有包涵Python的元素信息
Linux.difference_update(Python)
print(Linux)

# 删除某一个元素，当删除元素不存在时不会抛出异常信息，remove删除不存在元素时会抛出异常信息
Linux.discard("jkjk")
print(Linux)

# 如果两个集合有零交集则返回True。
d = Linux.isdisjoint(Python)
print(d)
# 如果两个集合有零交集则返回True
Linux.isdisjoint(Python)
print(d)

# 报告是否有其他集合包含此集合。
d = Linux.issubset(Python)
print(d)
# 清空集合内容
# Linux.clear()
# print(Linux)