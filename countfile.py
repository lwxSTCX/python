#encoding=utf-8
import os

result=[]

def get_all(cwd):
    get_dir =os.listdir(cwd) #遍历当前目录，获取文件列表
    for i in get_dir:
        sub_dir=os.path.join(cwd,i)  #把当前目录与现在的文件名加入路径
        if os.path.isdir(sub_dir):  #判断是否还是文件夹
            get_all(sub_dir)
        else:
            ax=os.path.basename(sub_dir)  #如果当前路径不是文件夹，则将文件名放入列表中
            result.append(ax)  #依次增加
            print(len(result))  #计数
            
if __name__=="__main__":
    cur_path=os.getcwd()  #获取当前目录
    get_all(cur_path)
    