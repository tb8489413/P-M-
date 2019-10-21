import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
while True:
    pos = mc.player.getTilePos()
    time.sleep(1)
    mc.postToChat("X="+str(pos.x)+" Y="+str(pos.y)+" Z="+str(pos.z))

