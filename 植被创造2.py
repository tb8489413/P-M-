import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
mc = minecraft.Minecraft.create()


while True:
    n1 = 18
    n2 = random.randint(0,3)

    n3 = 17
    n4 = random.randint(0,3)
    
    pos = mc.player.getTilePos()
    pos.z = pos.z + 4

    if n2 == n4:
        #创建第一层树叶
        mc.setBlocks(pos.x+2,pos.y+7,pos.z-1,pos.x+2,pos.y+7,pos.z+1,n1,n2)
        mc.setBlocks(pos.x+1,pos.y+7,pos.z-2,pos.x-2,pos.y+7,pos.z+2,n1,n2)

        #创建第二层树叶
        mc.setBlocks(pos.x+2,pos.y+8,pos.z-1,pos.x+2,pos.y+8,pos.z+1,n1,n2)
        mc.setBlocks(pos.x+1,pos.y+8,pos.z-2,pos.x-2,pos.y+8,pos.z+2,n1,n2)
        mc.setBlock(pos.x-2,pos.y+8,pos.z-2,0)

        #创建第三层树叶
        mc.setBlocks(pos.x+1,pos.y+9,pos.z-1,pos.x-1,pos.y+9,pos.z+1,n1,n2)
        mc.setBlock(pos.x-1,pos.y+9,pos.z-1,0)
        mc.setBlock(pos.x-1,pos.y+9,pos.z+1,0)

        #创建第四层树叶
        mc.setBlocks(pos.x+1,pos.y+10,pos.z-1,pos.x-1,pos.y+10,pos.z+1,n1,n2)
        mc.setBlock(pos.x-1,pos.y+10,pos.z-1,0)
        mc.setBlock(pos.x-1,pos.y+10,pos.z+1,0)
        mc.setBlock(pos.x+1,pos.y+10,pos.z-1,0)
        mc.setBlock(pos.x+1,pos.y+10,pos.z+1,0)

        #创建树干
        mc.setBlocks(pos.x,pos.y,pos.z,pos.x,pos.y+9,pos.z,n3,n4)

    time.sleep(3)
    
    
    
