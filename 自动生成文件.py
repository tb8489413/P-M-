import os
while True:
    choice = input('''请选择你要操作的方法
    1.创建文件
    2.删除文件
    3.退出系统
    >''')
    
    if choice == "1":
        #创建文件
        FileName = input("请输入你要创建的文件名：")
        FileFormat = input("请输入你要创建的文件格式：")
        FileNumStart = int(input("请输入你要创建的文件数量(起始编号)："))
        FileNumEnd = int(input("请输入你要创建的文件数量(结束编号)："))
        n = FileNumEnd+1 - FileNumStart

        for i in range(FileNumStart,FileNumEnd+1):
            file = open(r"C:\Users\郭良成\Desktop\play"+"\\"+FileName+str(i)+"."+FileFormat,"w")
            file.write("")
        file.close()
        print(str(n)+"个"+FileFormat+"文件已创建完成")
    
    if choice == "2":
        #删除文件
        FileName = input("请输入你要删除的文件名：")
        FileFormat = input("请输入你要删除的文件格式：")
        FileNumStart = int(input("请输入你要删除的文件数量(起始编号)："))
        FileNumEnd = int(input("请输入你要删除的文件数量(结束编号)："))
        n = FileNumEnd+1 - FileNumStart

        for i in range(FileNumStart,FileNumEnd+1):
            os.remove("C:\\Users\\郭良成\\Desktop\\play"+"\\"+FileName+str(i)+"."+FileFormat)
    
        print(str(n)+"个"+FileFormat+"文件已删除完成！")
        
    if choice == "*":
        #创建文件
        FileName = input("请输入你要创建的文件名：")
        FileFormat = input("请输入你要创建的文件格式：")
        FileNumStart = int(input("请输入你要创建的文件数量(起始编号)："))
        FileNumEnd = int(input("请输入你要创建的文件数量(结束编号)："))
        word = int(input("请输入你要写入的文件大小:1.KB;2.MB;3;GB"))
        n = FileNumEnd+1 - FileNumStart

        for i in range(FileNumStart,FileNumEnd+1):
            file = open(r"C:\Users\郭良成\Desktop\play"+"\\"+FileName+str(i)+"."+FileFormat,"a")

            for j in range(1024**word):
                file.write("*")
                
        file.close()
        print(str(n)+"个"+FileFormat+"哑铃文件已创建完成")
        
        

    if choice == "3":
        break
