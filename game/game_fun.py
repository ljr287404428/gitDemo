import math
import random


def fight(enemy_hp,enemy_power):
    #定义4个变量来存放数据
    my_hp = 1000
    my_power = 200

    #打印私人的血量和攻击力
    print(f"敌人的血量为{enemy_hp},攻击力为{enemy_power}")

    #加入循环，让游戏可以多轮
    while True:
        # 定义最终血量计算方式
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        #判断谁的血量小于等于0
        if my_hp <= 0:
            #打印我和敌人的剩余血量
            print(f"我的剩余血量为{my_hp}")
            print(f"敌人剩余血量为{enemy_hp}")
            print("我输了")
            break
        elif enemy_hp <=0:
            print(f"我的剩余血量为{my_hp}")
            print(f"敌人剩余血量为{enemy_hp}")
            print("我赢了")
            break

if __name__ == "__main__":
    hp = [x for x in range(990,1010)]
    print(hp)
    print(type(hp))
    #让敌人的hp从hp列表中随机挑选一个值
    enemy_hp = random.choice(hp)
    print(enemy_hp)
    #敌人的攻击力用fandint方法生成随机整数
    enemu_power = random.randint(190,210)
    print(enemy_hp)

    #调用函数，传入敌人的hp和power
    fight(enemy_hp,enemu_power)