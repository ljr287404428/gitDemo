"""
用类和面向对象的思想，“描述”生活中任意接触到的东西
（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
"""
#描述狗的类
class Dog:
    #构造方法，传入种类，颜色
    def __init__(self,dog_type,dog_colour):
        #种类
        self.dog_type = dog_type
        #颜色
        self.dog_colour = dog_colour

    #看门
    def watch_door(self):
        print(f"{self.dog_type}可以在家看门")
    #颜值
    def level_of_appearance(self):
        print(f"{self.dog_colour}的{self.dog_type}最可爱")

#公司类
class Company:
    #构造方法
    def __init__(self,company_name,company_nature):
        #公司名称
        self.company_name = company_name
        # 公司性质
        self.company_nature = company_nature

    #公司基本信息
    def information(self):
        print(f"{self.company_name}是{self.company_nature}的一个公司")
    #公司地址，传入公司地址company_address
    def address(self,company_address):
        print(f"{self.company_name}位于{company_address}")

#手机类
class Mobile_Phone:
    #构造方法，传入手机的型号model
    def __init__(self,model):
        self.model = model

    #所属品牌,传入品牌brand
    def modile_phone_brand(self,brand):
        print(f"{self.model}属于{brand}的手机")
    #手机综合评价，传入综合评分
    def modile_phone_evaluate(self,score):
        print(f"{self.model}的综合评分为{score}")

#学生类
class student:
    #构造方法，传入学生的姓名
    def __init__(self,name):
        self.name = name

    #学生的年级,传入学生的年级grade
    def student_grade(self,grade):
        print(f"{self.name}现在在上{grade}")
    #学生的学校，传入学生的学校名称school_name
    def student_school_name(self,school_name):
        print(f"{self.name}就读于{school_name}")

#游戏类
class game:
    #构造方法，传入游戏的英雄名称name
    def __init__(self,name):
        self.name = name

    #判断类型,传入类型type
    def hero_type(self,type):
        print(f"{self.name}属于{type}的英雄")
    #适合位置,传入位置参数position
    def hero_position(self,position):
        print(f"{self.name}适合打{position}")