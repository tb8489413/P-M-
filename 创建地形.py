#导入随机函数
import random
#导入时间函数
import time
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()


#创建地形
while True:
    #生成实心体
    height = random.randint(1,50)
    width = random.randint(1,20)
    length = random.randint(1,20)
    n = random.randint(0,6)
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x,pos.y,pos.z+1,pos.x+length,pos.y+height,pos.z+width,1,n)
##    time.sleep(1)
    #生成空心体
    height_1 = random.randint(1,5)
    width_1 = random.randint(1,5)
    length_1 = random.randint(1,5)
    mc.setBlocks(pos.x,pos.y,pos.z+1,pos.x+length_1,pos.y+height_1,pos.z+width_1,0)
##    time.sleep(1)
    
