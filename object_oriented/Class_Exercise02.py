#!/usr/bin/env python
# coding:utf-8

class Chinese:
    '''这里写文档注释'''
    area = "Asia"

    # def init(name,age,gender):
    #     dic={
    #         'name':name,
    #         'age':age,
    #         'gender':gender
    #     }
    #     return dic

    def __init__(self, name, age, gender):
        print("start...")
        self.aname = name
        self.aage = age
        self.agender = gender
        print("end...")
        ## 自动return None 所以，不能加return

    def dun(self):
        print("%s 亚洲蹲在 %s " % (self.aname, self.area))

    def speak(self, lang):
        print("%s 讲%s " % (self.aname, lang))


p1 = Chinese("Tom", 22, "male")  # 实例化
print(p1.__dict__)  # 查看实例的字典
print(p1.aname)
print(p1.agender)
print(p1.area)

p1.dun()
p1.speak('本地方言')
print(p1.area)

# 修改
Chinese.area = '东方大陆'


# 修改函数
def xia_dun(self):
    print("%s 坐在了地上。" % self.aname)


Chinese.dun = xia_dun  # 修改了类的内部函数

# 增加
Chinese.skin = 'yellow'

p2 = Chinese("小明", 11, "男")
print(p2.area)
print(p2.skin)
print(p1.skin)  # 之前的实例也可以用，因为实例是对类的引用
p2.dun()

# 删除
# del Chinese.area
# print(p2.area)
