# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/9 14:33
@Auth ： shijiron
@File ：scb21_lesson_01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
print("hello world")
# python代码标识符的命令规范（自己取名字的---变量，函数名）

"""
1.不能以数字开头
2.只能包含数字、字母以及下划线
3.不能用关键字命名
4.不能用python的内置函数命名
"""
#
# list_1 = []
# list_1.append(1)
# print(list_1)
# list_1.append(2)
# print(list_1)
# list_1.append(1)
# print(list_1)
# list_1.insert(1,"smc")
# print(list_1)


# del list_1[0]  # 知道索引 想删除啥删除啥？
# y = list_1[-1]
# print(y)
# i = list_1.pop(2)
# print(i)
# list_1.append("pws")
# list_1.insert(2, "hiu")
# print(list_1)
# list_1.pop(0)
# list_1.pop(2)
# list_1.pop(2)
# print(list_1)
# list_1.sort()
# print(list_1)
# list_1.sort(reverse=True)
# print(list_1)
# name = 1
# name1 = 2
# print(name, name1)
# for item in list_1:
#     print(item.title(), name)
#
# squres = []
# for value in range(1,11):
#     squre = value **2
#     squres.append(squre)
# print(squres)

# nums = []
# for new in range(1, 11 , 2):
#     num = new ** 2
#     nums.append(num)
#     print(nums)
#
# nums = []
# for new in range(1, 11):
#     nums.append(new ** 2)
# print(nums)
#
# print(min(nums))
# print(max(nums))
# print(sum(nums))
# nums = [value ** 2 for value in range(1, 11)]
# print(nums)

# for value in range(1, 1000000):
#     print(value)
# list_1 = [value for value in range(1, 1000001)]
# # print(list_1)
# print(min(list_1))
# print(max(list_1))

# list_1 = [value for value in range(1, 20, 2)]
# print(list_1)
# list_2 = []
# for value in range(1, 20,):
#     # list_1 = value
#
#     list_2.append(value)
# print(list_2)

# list_1 = []
# for value in range(1, 31):
#     if value // 3 == 0:
#         list_1.append(value)
# print(list_1)

# list_1 = [value ** 3 for value in range(1, 11)]
# print(list_1)
#
# list_2 = []
# for num in range(1, 11):
#     nums = num ** 3
#     list_2.append(nums)
# print(list_2)
# print(list_1[-3:])
# print(list_1[-3:-9:-1])
# name = "asdasd"
# print("sdasdasdasdasdasd", name)
# print(f"sdasdasdasdasdasd{name}")

# color = "green"
# if color == "yellow":
#     print("gain 5 score")
# elif color == "blue":
#     print("gain 10 score")
# elif color == "green":
#     print("gain 0 score")
#
# age = 10
# if age < 4:
#     print("幼儿")
# elif age < 13:
#     print("儿童")
# elif age < 20:
#     print("青少年")
# elif age < 65:
#     print("老年人")
#


dic_1 = {"name": "smc", "gender": "man"}
for k, v in dic_1.items():
    print(f'\nk:{k}')
    print(f'v:{v}')