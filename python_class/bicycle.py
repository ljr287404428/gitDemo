

#自行车类
class Bicycle:
    def run(self,km):
        print(f"一共用脚骑了{km}公里，累死了")

# 电动自行车类
# 继承把父类名称放在类名后面的小括号中
class EBicycle(Bicycle):
    # 属性需要传参定义，可以直接放到构造函数中
    def __init__(self,valume):
        self.valume = valume

    #充电的方法
    def fill_charge(self,vol):
        #充电后的电量 = 本身的电量 + 充电电量
        self.valume = self.valume + vol
        print(f"充了{vol}度电，现在的电量为{self.valume}度")

    #骑行方法
    def run(self,km):
        # 1.获取目前电量所能电动骑行的最大里程数
        power_km = self.valume * 10

        if power_km >= km:
            print(f"我使用电瓶电量骑行了{km}公里")
        else:
            # 电量不够了，在电用完之后，还得用脚骑行
            print(f"我使用电瓶电量骑行了{power_km}公里")
            # 当电量消耗尽时调用Bicycle的run方法骑行
            #非继承调用
            # bike = Bicycle()
            # bike.run(km - power_km)
            # 继承调用
            super().run(km - power_km)


# bike = Bicycle()
# #bike.run(10)
# ebike = EBicycle(10)
# ebike.fill_charge(3)

ebike = EBicycle(10)
ebike.run(150 )