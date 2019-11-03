import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time
import random
mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

pos = mc.player.getTilePos()
x = pos.x 
y = pos.y
z = pos.z

#创建模型参数(与我的世界建立连接，位置，模型内部坐标)
cz = 41
#模型内部坐标
mx1_blocks = [
    minecraftstuff.ShapeBlock(0,0,0,cz),
    minecraftstuff.ShapeBlock(1,1,0,cz),
    minecraftstuff.ShapeBlock(0,1,-1,cz),
    minecraftstuff.ShapeBlock(0,1,1,cz),
    minecraftstuff.ShapeBlock(1,1,0,cz),
    minecraftstuff.ShapeBlock(-1,1,0,cz),
    minecraftstuff.ShapeBlock(0,2,-1,cz),
    minecraftstuff.ShapeBlock(0,2,1,cz),
    minecraftstuff.ShapeBlock(1,2,0,cz),
    minecraftstuff.ShapeBlock(-1,2,0,cz),
    minecraftstuff.ShapeBlock(0,3,0,cz),        
    ]

mx2_blocks = [
    minecraftstuff.ShapeBlock(0,0,0,cz),
    minecraftstuff.ShapeBlock(1,1,0,cz),
    minecraftstuff.ShapeBlock(0,1,-1,cz),
    minecraftstuff.ShapeBlock(0,1,1,cz),
    minecraftstuff.ShapeBlock(1,1,0,cz),
    minecraftstuff.ShapeBlock(-1,1,0,cz),
    minecraftstuff.ShapeBlock(0,2,-1,cz),
    minecraftstuff.ShapeBlock(0,2,1,cz),
    minecraftstuff.ShapeBlock(1,2,0,cz),
    minecraftstuff.ShapeBlock(-1,2,0,cz),
    minecraftstuff.ShapeBlock(0,3,0,cz),        
    ]
#生成模型 
mx1 = minecraftstuff.MinecraftShape(mc,pos,mx1_blocks)
mx2 = minecraftstuff.MinecraftShape(mc,pos,mx1_blocks)

#模型运动
while True:
    x1 = random.randint(0,5)
    z1 = random.randint(0,5)
    y1 = random.randint(5,10)

    x2 = random.randint(0,5)
    z2 = random.randint(0,5)
    y2 = random.randint(5,10)
    
    time.sleep(0.5)
    mx1.move(x+x1,y1,z+z1)
    mx2.move(x+x2,y2,z+z2)
    if x1 == x and z1 == z:
        mc.player.setTilePos(x1,y1+1,z1)
        break
    if x2 == x and z2 == z:
        mc.player.setTilePos(x2,y2+1,z2)
        break
#清除模型    
mx.clear()
