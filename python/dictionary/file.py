import pandas as pd
import numpy as np
import re
import os

filename='a'
def file_check(file_name='英语单词记录.md'):
    
    exist=0
    path=os.path.dirname(__file__)
    for f_name in os.listdir(path):              #先查询当前文件目录中是否存在文件'英语单词记录.md'
        if file_name==f_name:
            exist=1
            break
    
    line=''
    word_file_exist=0
    word_file_name='单词路径.txt'
    word_file_dir=os.path.join(path,word_file_name)  #再查询当前目录中是否存在记录单词文件地址的文件'单词路径.txt'
    for f_name in os.listdir(path):
        if word_file_name==f_name:
            word_file_exist=1
            break
    if word_file_exist==1:
        with open(word_file_dir, 'r') as file:      #若存在则读取
            try:
                line = file.readline()
                '''
                有时候编码混乱会使得无法读取内容，进而报错
                '''
            except:
                print('文件路径存在问题！输入正确路径进行覆盖')
                exist=0
                return exist
    else:
        with open(word_file_dir, 'w') as file:      #若不存在，则创建
            pass
    if line == '':
        exist=0
    elif os.path.exists(line) is False:
        with open(word_file_dir, 'w') as file:     
            file.write('')
        exist=0
    else:
        exist=line
    return exist

def update_filename(fi):       #更新全局变量filename
    global filename
    filename=fi
    return filename
