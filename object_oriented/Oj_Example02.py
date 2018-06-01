#!/usr/bin/env python
# coding:utf-8

country = "中国"


class Chinese:
    '''这里写文档注释'''
    country = "China"

    li = ['a', 'b']

    def __init__(self, name):
        self.name = name
        print('-----------------', country)  # 这里的country只相当于普通的变量，跟类没有关系，因为没有通过点来调用

        # self.name = input("请输入用户名:") # 不建议在函数中使用输入输出。 混乱，可读性差

    def speak(self, lang):
        print("%s 讲%s " % (self.aname, lang))


p1 = Chinese('alex')
print("实例内调用", p1.country)  # 点的方式调用是从类的内部
print("类调用", Chinese.country)

print(p1.li)
# p1.li = [1,2,3]  # 实例的list被重新赋值
# print(p1.__dict__)  # 返回{'name': 'alex', 'li': [1, 2, 3]}
# print(Chinese.li)  # 返回 ['a', 'b']

p1.li.append('c')  # 附加了类中列表的元素
print(p1.__dict__)  # 实例的字典中没有 li 这个列表
print(Chinese.li)  # 类的列表被添加内容
