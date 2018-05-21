# coding=utf-8
# __author:Administrator
# __time:2018/5/21 12:43
# __file_name:staff_list

import io
import time
import os

FileRead = io.open('Staff_list', 'r', encoding='utf8')
Staff_list = eval(FileRead.read())
username = 0

'''
员工信息管理系统
需求：
1.增
2.删
3.改
4.查
5.管理员登陆
6.模糊搜索
'''

string = '''
        工号：%s
        姓名：%s
        年龄：%s
        部门：%s
        地址：%s
        电话：%s
         Q Q：%s
        微信：%s
        入职时间：%s
'''

Project = ['姓名', '年龄', '部门', '地址', '电话', 'qq', '微信', '入职时间']


def login():  # 登陆模块
    global username
    print
    '=' * 43, '员工信息管理系统', '=' * 43
    num = 1
    while num <= 3:
        username = int(raw_input('请输入你的工号：\n'))
        pwd = raw_input('请输入密码：\n')
        if username not in Staff_list:
            print
            '没有你的信息，请联系管理员添加或重新输入,还有 %d 次机会' % (3 - num)
            num += 1
        elif Staff_list[username]['权限'] == 1 and pwd == Staff_list[username]['密码']:
            print
            '欢迎 %s 进入员工信息管理系统' % Staff_list[username]['姓名']
            AdminMenuShow()
        elif Staff_list[username]['权限'] != 1 and pwd == Staff_list[username]['密码']:
            print
            '欢迎 %s 进入员工信息系统' % Staff_list[username]['姓名']
            StaffMenuShow()
        else:
            print
            '密码输入错误，还有 %d 次机会' % (3 - num)
            num += 1
    else:
        print
        '输入次数过多，已退出程序'
        time.sleep(3)
        exit()


def OptionJudge(chioce):  # 对用户输入进行判断
    if chioce == 'A' or chioce == 'a':
        Increase()
    elif chioce == 'B' or chioce == 'b':
        Delete()
    elif chioce == 'C' or chioce == 'c':
        Amend()
    elif chioce == 'D' or chioce == 'd':
        Query()
    elif chioce == 'E' or chioce == 'e':
        AllStaff()
    elif chioce == 'F' or chioce == 'f':
        Search()
    elif chioce == 'G' or chioce == 'g':
        IncreaseAdmin()
    elif chioce == 'H' or chioce == 'h':
        exit()
    else:
        chioce = raw_input('你的输入有误 请重新输入:\n')
        OptionJudge(chioce)


def AdminMenuShow():  # 管理员菜单展示
    print
    '=' * 43, '员工信息管理系统', '=' * 43
    print
    '【A】增加一个成员  【B】删除一个成员'
    print
    '【C】修改一个成员  【D】查询一个成员'
    print
    '【E】查看所有成员  【F】关键词搜索  '
    print
    '【G】增加一个管理员【H】退出系统'
    print
    chioce = raw_input('请输入你的选择：\n')
    OptionJudge(chioce)


def StaffMenuShow():  # 普通用户菜单展示
    print
    '=' * 43, '员工信息管理系统', '=' * 43
    print
    '【E】查看所有成员  【D】查询一个成员'
    print
    '【F】关键词搜索    【H】退出系统                '
    chioce = raw_input('请输入你的选择：\n')
    OptionJudge(chioce)


def Increase():  # 增加一个用户
    print
    '=' * 44, '增加新的员工', '=' * 44
    staff_num = Staff_list['num']
    Staff_list[staff_num] = {}
    Staff_list[staff_num]['姓名'] = raw_input('请输入员工姓名\n')
    Staff_list[staff_num]['年龄'] = raw_input('请输入员工年龄\n')
    Staff_list[staff_num]['部门'] = raw_input('请输入员工部门\n')
    Staff_list[staff_num]['住址'] = raw_input('请输入员工地址\n')
    Staff_list[staff_num]['电话'] = raw_input('请输入员工电话号码\n')
    Staff_list[staff_num]['qq'] = raw_input('请输入员工QQ号码\n')
    Staff_list[staff_num]['微信'] = raw_input('请输入员工微信号码\n')
    Staff_list[staff_num]['入职时间'] = raw_input('请输入员工入职日期\n')
    Staff_list[staff_num]['密码'] = raw_input('请设置员工登陆密码\n')
    Staff_list[staff_num]['权限'] = raw_input('请设置员工权限\n')
    Staff_list['num'] = Staff_list['num'] + 1
    print
    '%s已录入成功，工号为%d' % (Staff_list[staff_num]['姓名'], staff_num)
    Staff_list_UpDate()


def IncreaseAdmin():  # 创建管理员账户
    print
    '=' * 43, '正在增加管理员', '=' * 43
    staff_num = int(raw_input('请输入员工工号\n'))
    if Staff_list[staff_num] == {}:
        print
        '工号为%d的员工已离职，请重新输入' % staff_num
        IncreaseAdmin()
    elif staff_num in Staff_list and Staff_list[staff_num] != {}:
        Flag = raw_input('确认是否将 %s 设置为管理员用户？Y/N' % Staff_list[staff_num]['姓名'])
        if Flag == 'Y':
            print
            '%s 已成功设置为管理员' % Staff_list[staff_num]['姓名']
            Staff_list[staff_num]['权限'] = 1
            time.sleep(3)
            Staff_list_UpDate()
        elif Flag == 'N':
            print
            '正在返回主菜单'
            AdminMenuShow()
        else:
            print
            '你的输入错误，正在为你返回主菜单'
            AdminMenuShow()
    else:
        print
        '没有工号为%d的员工，请重新输入' % staff_num
        IncreaseAdmin()


def Delete():  # 删除一个用户
    print
    '=' * 46, '删除员工', '=' * 46
    Staff_num = int(raw_input('请输入你要删除的员工工号\n'))
    if Staff_num in Staff_list and Staff_list[Staff_num] != {}:
        Flag = raw_input('确认是否删除 %s？Y/N ' % Staff_list[Staff_num]['姓名'])
        if Flag == 'Y' or Flag == 'y':
            temp = Staff_list[Staff_num]['姓名']
            Staff_list[Staff_num] = {}
            time.sleep(3)
            print
            '已经为您删除 %s' % temp
            Staff_list_UpDate()
        elif Flag == 'N' or Flag == 'n':
            print
            '请重新输入'
            Delete()
        else:
            print
            '你的输入错误，正在为你返回主菜单'
            AdminMenuShow()
    elif Staff_num in Staff_list and Staff_list[Staff_num] == {}:
        print
        '%s已被删除，请重新输入' % Staff_list[Staff_num]['姓名']
        Delete()
    else:
        print
        '没有工号为%d的用户，请重新输入' % Staff_num
        Delete()
    print
    '操作完毕，正在返回主菜单'
    AdminMenuShow()


def Amend():  # 修改一个用户
    print
    '=' * 44, '修改员工信息', '=' * 44
    staff_num = int(raw_input('请输入你要修改的员工编号\n'))
    if staff_num not in Staff_list:
        print
        '你输入的员工编号不存在，请重新输入'
        Amend()
    elif staff_num == 0:
        print
        '你无权修改,请重新输入'
        Amend()
    elif Staff_list[staff_num] == {}:
        print
        '你所要修改的员工已被删除，无法进行修改'
        Amend()
    else:
        while True:
            project = raw_input('请输入你要修改的项目（姓名/年龄/部门/地址/电话/qq/微信/入职时间）\n')
            if project in Staff_list[staff_num] and project in Project:
                content = raw_input('请输入你要修改的内容：\n')
                Staff_list[staff_num][project] = content
                print
                '已为您修改完毕，正在为您返回主菜单'
                Staff_list_UpDate()
            else:
                print
                '你输入的项目不正确，请重新输入'


def Permissions():
    if Staff_list[username]['权限'] == 1:
        print
        '操作完毕，正在返回主菜单'
        AdminMenuShow()
    else:
        print
        '操作完毕，正在返回主菜单'
        StaffMenuShow()


def Query():  # 查询一个用户
    print
    '=' * 44, '员工信息查询', '=' * 44
    staff_num = int(raw_input('请输入员工工号\n'))
    if Staff_list[staff_num] == {}:
        print
        '该员工已被删除，请重新搜索你要查询的员工'
        Query()
    elif staff_num in Staff_list:
        print
        '=' * 43, 'Info of %s' % Staff_list[staff_num]['姓名'], '=' * 43
        print
        string % (
            staff_num, Staff_list[staff_num]['姓名'], Staff_list[staff_num]['年龄'], Staff_list[staff_num]['部门'],
            Staff_list[staff_num]['住址'], Staff_list[staff_num]['电话'], Staff_list[staff_num]['qq'],
            Staff_list[staff_num]['微信'], Staff_list[staff_num]['入职时间'])
    else:
        print
        '没有工号为%d的员工，请重新输入'
        Query()
    Flag = raw_input('员工%s 信息已查询完毕，是否返回主菜单？Y/N ' % Staff_list[staff_num]['姓名'])
    if Flag == 'Y' or Flag == 'y':
        Permissions()
    else:
        print
        '重新查询一个用户'
        Query()


def AllStaff():  # 查看所有用户
    for i in range(1, Staff_list['num']):
        if Staff_list[i] == {}:
            print
            '=' * 45, '第%d 号员工' % i, '=' * 45
            print
            '第%d 号员工已离职' % i
        else:
            print
            '=' * 44, '%s的信息' % Staff_list[i]['姓名'], '=' * 44,
            print
            string % (
                i, Staff_list[i]['姓名'], Staff_list[i]['年龄'], Staff_list[i]['部门'],
                Staff_list[i]['住址'], Staff_list[i]['电话'], Staff_list[i]['qq'],
                Staff_list[i]['微信'], Staff_list[i]['入职时间'])
    Flag = raw_input('用户信息已查询完毕，是否返回主菜单？Y/N ')
    if Flag == 'Y' or Flag == 'y':
        Permissions()
    else:
        print
        '不允许操作'


def Search():  # 关键词搜索
    print
    '=' * 44, '员工信息搜索', '=' * 44
    project = raw_input('请输入你要查找的项目（姓名/年龄/部门/地址/电话/qq/微信/入职时间）\n')
    num = 0
    while True:
        key = raw_input('请输入你要查找的关键字\n')
        if project in Project:
            for i in range(1, Staff_list['num']):
                if Staff_list[i] == {}:
                    pass
                elif key in Staff_list[i][project]:
                    print
                    '=' * 44, '%s的信息' % Staff_list[i]['姓名'], '=' * 44,
                    print
                    string % (
                        i, Staff_list[i]['姓名'], Staff_list[i]['年龄'], Staff_list[i]['部门'],
                        Staff_list[i]['住址'], Staff_list[i]['电话'], Staff_list[i]['qq'],
                        Staff_list[i]['微信'], Staff_list[i]['入职时间'])
                    num += 1
            if num == 0:
                print
                '没有搜索到结果，请重新搜索'
            else:
                print
                '共搜索到 %d 名 %s 为 %s 的员工' % (num, project, key)
                Flag = raw_input('用户信息已查询完毕，任意键继续搜索，选择Y返回主菜单 ')
                if Flag == 'Y' or Flag == 'y':
                    Permissions()
                else:
                    Search()
        else:
            print
            '你要查找的项目不存在'


def Staff_list_UpDate():
    global FileRead
    FileRead.close()
    with open('Staff_list_copy', 'w') as FileWrite:
        Write_Staff_list = str(Staff_list)
        FileWrite.write(Write_Staff_list)
    os.remove('Staff_list')
    os.renames('Staff_list_copy', 'Staff_list')
    FileRead = io.open('Staff_list', 'r', encoding='utf8')
    time.sleep(3)
    AdminMenuShow()


login()
