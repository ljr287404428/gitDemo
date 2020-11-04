
class Game:
    def __init__(self,my_hp,enemy_hp):
        # 定义4个变量来存放数据
        self.my_hp = my_hp
        self.my_power = 200
        self.enemy_hp = enemy_hp
        self.enemy_power = 199

    def fight(self):
        # 加入循环，让游戏可以多轮
        while True:
            # 定义最终血量计算方式
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            # 判断谁的血量小于等于0
            if self.my_hp <= 0:
                # 打印我和敌人的剩余血量
                print(f"我的剩余血量为{self.my_hp}")
                print(f"敌人剩余血量为{self.enemy_hp}")
                print("我输了")
                break
            elif self.enemy_hp <= 0:
                print(f"我的剩余血量为{self.my_hp}")
                print(f"敌人剩余血量为{self.enemy_hp}")
                print("我赢了")
                break
    # 休息方法
    def rest(self,time_num):
        print(f"太累了，休息{time_num}分钟")

class HouYi(Game):
    #定义护甲属性
    def __init__(self,my_hp,enemy_hp):
        self.defense = 100
        # 通过继承调用父类的构造函数，拿到父类的属性
        super().__init__(my_hp,enemy_hp)
    #改造fight方法
    def fight(self):
        while True:
            # 定义最终血量计算方式
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            # 判断谁的血量小于等于0
            if self.my_hp <= 0:
                # 打印我和敌人的剩余血量
                print(f"我的剩余血量为{self.my_hp}")
                print(f"敌人剩余血量为{self.enemy_hp}")
                print("我输了")
                break
            elif self.enemy_hp <= 0:
                print(f"我的剩余血量为{self.my_hp}")
                print(f"敌人剩余血量为{self.enemy_hp}")
                print("我赢了")
                break


# game = Game()
# game.fight()
houyi = HouYi(1000,1300)
houyi.fight()
houyi.rest(3)