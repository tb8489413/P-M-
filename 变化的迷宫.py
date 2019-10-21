import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time
import random
mc = minecraft.Minecraft.create()
def qing_kong():
    mc.setBlocks(0,0,0,100,5,100,0)

def h_j():
    n1 = random.randint(0,15)
    x1 = random.randint(0,100)
    z1 = random.randint(0,100)
    z2 = random.randint(0,100)

    if x1 == 50 and z1 == 50:
        n1 = 49
    elif x1 ==50 and z2 == 50:
        n1 = 49
    else:
        n1 = random.randint(0,15)
                
    mc.setBlocks(x1,0,z1,x1,4,z2,95,n1)
def h_x():
    x3 = random.randint(0,100)
    z3 = random.randint(0,100)
    z4 = random.randint(0,100)
    mc.setBlocks(x3,0,z3,x3,4,z4,0)

def s_j():
    n2 = random.randint(0,15)
    x5 = random.randint(0,100)
    x6 = random.randint(0,100)
    z5 = random.randint(0,100)

    if x5 ==50 and z5 == 50:
        n2 = 49
    elif x6 ==50 and z5 == 50:
        n2 = 49
    else:
        n2 = random.randint(0,15)
        
    mc.setBlocks(x5,0,z5,x6,4,z5,95,n2)
    
def s_x():
    x5 = random.randint(0,100)
    x6 = random.randint(0,100)
    z5 = random.randint(0,100)
    mc.setBlocks(x5,0,z5,x6,4,z5,0)

def c_s():
    pos = mc.player.getTilePos()
    if pos.x == 0 and pos.y == 0 and pos.z == -9:
        mc.postToChat("transmit.......")
        time.sleep(3)
        mc.player.setPos(50,0,50)
        mc.postToChat("Welcome to my maze!")
    
qing_kong()
time.sleep(3)
while True:
    c_s()
    h_j()
    s_j()
    time.sleep(0.1)
    h_x()
    s_x()
    time.sleep(0.1)
