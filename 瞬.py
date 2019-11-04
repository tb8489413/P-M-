import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()

    x = pos.x
    y = pos.y
    z = pos.z

    #树林坐标5,0,-13
    #家坐标-36,0,65
    #危险地带58,0,17
    #中转站（瞬）-15,0,9

    if x == -15 and y == 0 and z == 9:
        print("欢迎使用【瞬】")
        
        #用户交互
        n = int(input("请选择你要去的地点：1.树林 2.家 3.危险地带"))

        if n == 1:
            #传送
            mc.player.setTilePos(5,0,-13)
        elif n == 2:
            mc.player.setTilePos(-36,0,65)
        elif n == 3:
            mc.player.setTilePos(58,0,17)
