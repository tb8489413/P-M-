import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

#用户交互
x1 = int(input("请输入要清除区域的x1:"))
y1 = int(input("请输入要清除区域的y1:"))
z1 = int(input("请输入要清除区域的z1:"))

x2 = int(input("请输入要清除区域的x2:"))
y2 = int(input("请输入要清除区域的y2:"))
z2 = int(input("请输入要清除区域的z2:"))

n1 = int(input("请输入方块ID:"))
n2 = int(input("请输入方块Data ID:"))

#清除区域
mc.setBlocks(pos.x+x1,pos.y+y1,pos.z+z1,pos.x+x2,pos.y+y2,pos.z+z2,n1,n2)
