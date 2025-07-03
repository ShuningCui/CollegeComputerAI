# 15. Craps游戏模拟 。
# 游戏规则如下:
# 游戏2人玩，通过掷2枚骰子决定输赢，一方位庄家，一方为玩家。
# 在一局中，始终由玩家掷骰子。每个骰子有6个面，包含1-6点。
# 等2枚骰子停止转动后，计算两个朝上面的点数之和。
# 如果第一次掷出的点数和为7或者11，则玩家胜。
# 如果点数为2，3或者12（称Craps），庄胜。
# 如果第一次掷出的点数和为4，5，6，8，9或10则该点数为玩家所需要的“正点”。
# 玩家继续掷骰子，直到再次出现该“正点”，则玩家胜。
# 如果在玩家再次掷出“正点”之前出现了点数7，则庄胜。

import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

player = roll_dice()
if player in [7, 11]:
    print("玩家胜")
elif player in [2, 3, 12]:
    print("庄胜")
else:
    print("正点为", player)
    while True:
        player = roll_dice()
        if player == 7:
            print("庄胜")
            break
        elif player == player:
            print("玩家胜")
            break
        else:
            print("继续掷骰子")
            continue



