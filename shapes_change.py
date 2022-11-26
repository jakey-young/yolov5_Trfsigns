"""
作者：97438
日期：2022年11月25日
"""
from PIL import Image
import os.path
import glob

# 定义图像分辨率转换函数
def convertjpg(jpgfile, outdir, width=640, height=640):
    img = Image.open(jpgfile) # 打开原图像文件夹
    try:
        new_img = img.resize((width, height), Image.Resampling.BILINEAR) # 重置图像宽和高
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))    # 保存新格式图片
    except Exception as e: # 报错提示
        print(e)


if __name__ == "__main__":
    print("开始运行")
    for jpgfile in glob.glob(r'D:\PycharmProjects\yolodata\shapechange\*.jpg'):
        convertjpg(jpgfile, r'D:\PycharmProjects\yolodata\aftershapechange')