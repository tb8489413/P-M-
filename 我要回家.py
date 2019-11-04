import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

##while True:
##    pos = mc.player.getTilePos()
##    print(pos)
##    time.sleep(0.5)

pos = mc.player.getTilePos()    
#家的坐标-36,0,65
#传送的指令
time.sleep(3)
mc.player.setTilePos(-36,0,65)
print("欢迎回家！")
    
    
    
