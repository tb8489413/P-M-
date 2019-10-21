import mcpi.minecraft as minecraft
#导入方块模块
import mcpi.block as block
mc = minecraft.Minecraft.create()

#获取玩家坐标
pos = mc.player.getTilePos()

#打印玩家坐标
print(pos)

#生成一个方块(绝对坐标)
##mc.setBlock(14,0,-5,1,2)
mc.setBlock(pos.x+2,pos.y,pos.z,1)
