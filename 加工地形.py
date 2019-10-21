#导入随机函数
import random
#导入时间函数
import time
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    #生成空气方块
    mc.setBlocks(pos.x+1,pos.y,pos.z,pos.x+1,pos.y+2,pos.z,0)#前
    mc.setBlocks(pos.x-1,pos.y,pos.z,pos.x-1,pos.y+2,pos.z,0)#后
    mc.setBlocks(pos.x,pos.y,pos.z-1,pos.x,pos.y+2,pos.z-1,0)#左
    mc.setBlocks(pos.x,pos.y,pos.z+1,pos.x,pos.y+2,pos.z+1,0)#右
    #生成矿灯
    mc.setBlock(pos.x,pos.y+2,pos.z,169)
