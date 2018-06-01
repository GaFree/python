#!/usr/bin/env python
# coding:utf-8

## 类：把一类事物的相同的特征和动作整合到一起就是类，类是一个抽象的概念
## 对象：就是基于类而创建的一个具体的事物（具体存在的）也是特征和动作整合到一起

# class Chinese: # 经典类 python2中的区分
#     '''这是一个中国人的类'''
#     pass
#
# print(Chinese)
#
#
# class Chinese(object): # 新式类 python2中的区分
#     pass

# 实例化到底干了什么？
# p1 = Chinese()  # 实例化 并不像其它语言使用new
# print(p1)


## python3中不再区分，都是新式类
class Chinese:
    '''这里写文档注释'''
    # 1 数据属性
    area = "Asia"

    # 2 函数属性
    def dun():
        print("亚洲蹲")

    def speak(self):
        print("讲汉语 %s" % self)


print(dir(Chinese))
print(Chinese.__dict__)  # 查看类的属性字典，字典里存放着类的数据属性和函数属性

print(Chinese.area)
Chinese.dun()  # 直接执行类中的函数
Chinese.__dict__['dun']()  # 通过字典方式调用类中函数
Chinese.__dict__['speak']("你好")

print(Chinese.__name__)  # 类名
print(Chinese.__doc__)  # 类的文档注释
print(Chinese.__base__)  # 基类 <class 'object'>
print(Chinese.__bases__)  # 基类 (<class 'object'>)
print(Chinese.__module__)  # 来自模块
