"""
1用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
2定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
    see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，
    如果传入“丁春秋”，打印“叛徒！我杀了你”
    fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，
    打完之后，比较双方血量。血多的一方获胜。
    定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
    加入模块化改造
"""
#定义一个天山童姥类
class TongLao:
    #构造方法，传入属性血量、武力值
    def __init__(self,blood_volume,force_value):
        #血量属性
        self.blood_volume = blood_volume
        #武力值属性
        self.force_value = force_value
    #定义see_people方法,传入一个name参数
    def see_people(self,name):
        #如果输入的是“WYZ”，则打印“师弟！！！”
        if name == "WYZ":
            print("师弟！！！")
        #如果输入的是“李秋水”，则打印“师弟是我的！”
        elif name == "李秋水":
            print("师弟是我的！")
        #如果输入的是“丁春秋”,则打印“叛徒！我杀了你”
        elif name == "丁春秋":
            print("叛徒！我杀了你")
        #如果输入的是其他内容，则打印“请重新输入”
        else:
            print("请重新输入")
    #fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，
    #打完之后，比较双方血量。血多的一方获胜。
    def fight_zms(self,hp,power):
        #将自身的血量缩减2倍
        self.blood_volume = self.blood_volume // 2
        #将自身的武力值提升10倍
        self.force_value = self.force_value * 10
        # 定义最终血量计算方式
        self.blood_volume = self.blood_volume - power
        hp = hp - self.force_value
        #如果自己的血量大于敌人的血量时，则自己获胜
        if self.blood_volume > hp :
            print("我赢了")
        #如果自己的血量等于敌人的血量时，则平手
        elif self.blood_volume == hp :
            print("平手")
        #否则，就是敌人获胜
        else :
            print("敌人获胜")