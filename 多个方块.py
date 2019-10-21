import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

#生成多个方块
mc.setBlocks(pos.x+1,pos.y,pos.z,pos.x+1+9,pos.y+9,pos.z+9,41)
