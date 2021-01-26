#coding=utf-8
from PIL import Image
import numpy as np
import random
import os
def Jpg(dir_line):
    try:
        im=Image.open(dir_line)
    except IOError as er_info:
        print er_info
        exit()

    y=im.size[0]
    x=im.size[1]
    img=im.load()
    c = Image.new("RGB",(x,y))
    for i in range (0,x):
        for j in range (0,y):
            w=x-i-1
            h=y-j-1
            rgb=img[j,i]#翻转90度
            c.putpixel([i,j],rgb)
    '''
    x=im.size[0]
    y=im.size[1]
    img=im.load()
    c = Image.new("RGB",(x,y))
    for i in range (0,x):
        for j in range (0,y):
            w=x-i-1
            h=y-j-1
            rgb=img[w,j] #镜像翻转
            rgb=img[w,h] #翻转180度
            rgv=img[i,h] #上下翻转
            c.putpixel([i,j],rgb)
    '''
    #c.show()
    c1 = c.transpose(Image.ROTATE_270)   # 引用固定的常量值
    return c1
if __name__=="__main__":
    img_path='./img/'
    save_path='./img_mirror/'
    img_list=os.listdir(img_path)
    for file in img_list:
        c1=Jpg(img_path+file)
        c1.save(save_path+'mirror_'+file)
        print(file+'      Done!     ')

