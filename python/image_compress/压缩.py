import os
from PIL import Image

def compress_image(infile, outfile='', mb=1500, step=10, quality=80):
    """不改变图片尺寸压缩到指定大小
    :param infile: 压缩源文件
    :param outfile: 压缩文件保存地址，为jpeg格式
    :param mb: 压缩目标，以kb为单位
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """
    o_size = os.path.getsize(infile)/1024
    if o_size <= mb:
        im = Image.open(infile)
        rgb_im = im.convert('RGB')
        rgb_im.save(outfile)
    while o_size > mb:
        im = Image.open(infile)
        rgb_im = im.convert('RGB')
        rgb_im.save(outfile, quality=quality)
        if quality - step < 0:
            break
        quality -= step
        o_size = os.path.getsize(outfile)/1024
    return outfile, os.path.getsize(infile)/1024,os.path.getsize(outfile)/1024        

infile_path="D:/vscode_file/vscode_file/python/image_compress/infile"           #输入图片文件夹
outfile_path="D:/vscode_file/vscode_file/python/image_compress/outfile"         #输出图片文件夹
files=os.listdir(infile_path)                           #得到指定文件夹中全部文件名（默认没有子文件夹）
print(files)
for num,file in enumerate(files):
    infile=infile_path+'/'+file
    outfile=outfile_path+'/'+os.path.splitext(file)[0]+'.jpeg'
    a,b,c=compress_image(infile,outfile)
    print(num+1,':',a,'    ',b,'    ',c)
print('all over!!')