#!/usr/bin/env python
# coding:utf-8

class Chinese:
    '''这里写文档注释'''
    country = "China"

    def __init__(self, name):
        self.aname = name

    def speak(self, lang):
        print("%s 讲%s " % (self.aname, lang))


p1 = Chinese('alex')
print(p1.__dict__)

# 查看
print(p1.speak)  # 只得到实例中函数的内存地址
p1.speak('汉语')

# 增加实例中的属性
p1.age = 18
print(p1.__dict__)
print(p1.age)

# 不要修改实例的函数属性，虽然可以操作。因为不规范
# 可以通过__dict__的方式更改字典，但是也不建议这么做，因为不稳定。

# 删除
del p1.age
print(p1.__dict__)

# 分清类和实例
p1.country = "zh"
print(Chinese.country)  # 这是类的
print(p1.country)  # 这是实例的
