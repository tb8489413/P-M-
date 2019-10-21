import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time
import random
mc = minecraft.Minecraft.create()
def qing_kong():
    mc.setBlocks(-1,-1,-1,101,5,101,0)
    
def wai_wei():
    mc.setBlocks(-1,-1,-1,101,4,101,49)
    mc.setBlocks(-1+1,-1+1,-1+1,101-1,4,101-1,0)
    mc.setBlocks(0,-1,0,100,-1,100,155)
    
def h_j():
    x1 = random.randint(0,100)
    z1 = random.randint(0,100)
    z2 = random.randint(0,100)        
    mc.setBlocks(x1,0,z1,x1,4,z2,49)
def h_x():
    x3 = random.randint(0,100)
    z3 = random.randint(0,100)
    z4 = random.randint(0,100)
    mc.setBlocks(x3,0,z3,x3,4,z4,0)

def s_j():
    x5 = random.randint(0,100)
    x6 = random.randint(0,100)
    z5 = random.randint(0,100)      
    mc.setBlocks(x5,0,z5,x6,4,z5,49)
    
def s_x():
    x5 = random.randint(0,100)
    x6 = random.randint(0,100)
    z5 = random.randint(0,100)
    mc.setBlocks(x5,0,z5,x6,4,z5,0)

    
qing_kong()
time.sleep(5)
wai_wei()
while True:
    h_j()
    s_j()
    time.sleep(0.1)
    h_x()
    s_x()
    time.sleep(0.1)
