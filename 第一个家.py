import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

#生成实体建筑
##mc.setBlocks(pos.x+1,pos.y,pos.z,pos.x+1+9,pos.y+9,pos.z+9,45)

#生成空心体建筑
##mc.setBlocks(pos.x+1+1,pos.y+1,pos.z+1,pos.x+1+9-1,pos.y+9-1,pos.z+9-1,0)

#生成门
##mc.setBlocks(pos.x+1,pos.y+1,pos.z+4,pos.x+1,pos.y+2,pos.z+5,324)

#生成窗
##mc.setBlocks(pos.x+1,pos.y+1+1,pos.z+1,pos.x+1,pos.y+2,pos.z+2,102)
##mc.setBlocks(pos.x+1,pos.y+1+1,pos.z+7,pos.x+1,pos.y+2,pos.z+8,102)

#生成隔板
mc.setBlocks(pos.x+1+1,pos.y+4,pos.z+1,pos.x+1+9-1,pos.y+4,pos.z+9-1,5)
