#导入随机函数
import random
#导入时间函数
import time
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

while True:
    pos = mc.player.getTilePos()
    #生成空气方块
    mc.setBlocks(pos.x+1,pos.y,pos.z,pos.x+1,pos.y+2,pos.z,0)#前
    mc.setBlocks(pos.x-1,pos.y,pos.z,pos.x-1,pos.y+2,pos.z,0)#后
    mc.setBlocks(pos.x,pos.y,pos.z-1,pos.x,pos.y+2,pos.z-1,0)#左
    mc.setBlocks(pos.x,pos.y,pos.z+1,pos.x,pos.y+2,pos.z+1,0)#右
    #生成矿灯
    mc.setBlock(pos.x+1,pos.y+2,pos.z,169)
    #消除头顶方块
    mc.setBlock(pos.x,pos.y+2,pos.z,0)
    #消除矿灯周围方块
    mc.setBlock(pos.x+2,pos.y+2,pos.z,0)
    mc.setBlock(pos.x+1,pos.y+2,pos.z-1,0)
    mc.setBlock(pos.x+1,pos.y+2,pos.z+1,0)
    mc.setBlock(pos.x+1,pos.y+3,pos.z,0)


