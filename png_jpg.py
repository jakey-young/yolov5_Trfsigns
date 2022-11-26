"""
作者：97438
日期：2022年11月25日
"""
import os
from PIL import Image
# 定义格式转化函数
def png_to_jpg(dirname_read, dirname_write, count=0):
    names = os.listdir(dirname_read)                  # 读取并保存原数据集文件夹下的图片
    for name in names:                                # 遍历图片
        img=Image.open(dirname_read + '\\'+ name)     # 生成每张图片的路径
        name=name.split(".")                          # 以 . 分割出图像格式后缀
        if name[-1] == "png":                         # 格式转化
            name[-1] = "jpg"
            name = str.join(".", name)
            to_save_path = dirname_write +'\\'+ name  # 新格式图片保存
            img.save(to_save_path)
            count+=1
            print(to_save_path, "------conut：",count)
        else:
            continue


if __name__ == "__main__":
    dirname_read = 'D:\PycharmProjects\yolov5-6.2\mytrain0'
    dirname_write = 'D:\PycharmProjects\yolov5-6.2\mytrain1'
    png_to_jpg(dirname_read, dirname_write, count=0)