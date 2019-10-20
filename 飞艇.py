import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time
mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
pos = mc.player.getTilePos()

#飞艇主体
for i in range(51):
    mcdrawing.drawCircle(pos.x,pos.y+50,pos.z+i,10,42)
for j in range(10):
    mcdrawing.drawCircle(pos.x,pos.y+50,pos.z+50+j,10-j,42)
for k in range(10):
    mcdrawing.drawCircle(pos.x,pos.y+50,pos.z-k,10-k,42)
    
#飞艇尾翼
wy_1 = []
wy_1.append(minecraft.Vec3(pos.x,pos.y+50+10,pos.z+40))
wy_1.append(minecraft.Vec3(pos.x,pos.y+50+10+5,pos.z+50))
wy_1.append(minecraft.Vec3(pos.x,pos.y+50+10+9,pos.z+50+8))
wy_1.append(minecraft.Vec3(pos.x,pos.y+50+2,pos.z+50+8))
mcdrawing.drawFace(wy_1,True,42)

wy_2 = []
wy_2.append(minecraft.Vec3(pos.x,pos.y+50-10,pos.z+40))
wy_2.append(minecraft.Vec3(pos.x,pos.y+50-10-5,pos.z+50))
wy_2.append(minecraft.Vec3(pos.x,pos.y+50-10-9,pos.z+50+8))
wy_2.append(minecraft.Vec3(pos.x,pos.y+50-2,pos.z+50+8))
mcdrawing.drawFace(wy_2,True,42)

wy_3 = []
wy_3.append(minecraft.Vec3(pos.x+10,pos.y+50,pos.z+40))
wy_3.append(minecraft.Vec3(pos.x+15,pos.y+50,pos.z+50))
wy_3.append(minecraft.Vec3(pos.x+19,pos.y+50,pos.z+50+8))
wy_3.append(minecraft.Vec3(pos.x+2,pos.y+50,pos.z+50+8))
mcdrawing.drawFace(wy_3,True,42)

wy_4 = []
wy_4.append(minecraft.Vec3(pos.x-10,pos.y+50,pos.z+40))
wy_4.append(minecraft.Vec3(pos.x-15,pos.y+50,pos.z+50))
wy_4.append(minecraft.Vec3(pos.x-19,pos.y+50,pos.z+50+8))
wy_4.append(minecraft.Vec3(pos.x-2,pos.y+50,pos.z+50+8))
mcdrawing.drawFace(wy_4,True,42)

