#导入我的世界模块
import mcpi.minecraft as minecraft
#与我的世界建立通讯链接
mc = minecraft.Minecraft.create()

#向聊天窗口发送信息
mc.postToChat("Hello World")
