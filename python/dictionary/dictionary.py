import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re

def get_CN(word):
    root_url = 'https://www.youdao.com/result?word='
    url = root_url +  word + '&lang=en' # 拼接URL
    response = requests.get(url)
    # 检查请求是否成功
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 通过标签、类名等选择器找到目标元素
        target_element = soup.find('ul', class_='basic')
        # 打印目标元素的文本内容或其他属性
        if target_element:
            #print(target_element)
            pass
        else:
            print('未找到目标元素')
    else:
        print('请求失败，状态码:', response.status_code)
    meanings = target_element.find_all(class_='word-exp')
    
    dic=[word]
    for i in range(len(meanings)):
        dic.append(meanings[i].get_text())     # 获取文本内容
        
    dic.insert(1,i+1)
    return dic   #返回的dic为列表[word,含义的数量,含义1,含义2,...]
    
def filter_string(text):
    filtered_text=re.sub('\d*',"",text)
    filtered_text=re.sub('\s*\.\s*',"",filtered_text)
    filtered_text=re.sub(r'\n',"",filtered_text)
    #filtered_text=re.sub('\s',"",text)
    return filtered_text

def read_from_date(date):
    filename='E:/vscode_file/vscode_file/markdown/英语学习/词汇记录.md'
    lines=[1]
    with open(filename, 'r') as file:
        line = file.readline()
        on=0
        while line:
            
            if re.match('\w*###\s'+date, line) and on is 0:
                #print('匹配到对应日期')
                on=1
            
            elif  (re.match('\w*###\w*', line) or re.match('\w*##\w*', line) or re.match('\w*#\w*', line))  and on is 1:
                #print('匹配到下一个日期')
                on=0
                break
            
            if re.match('\w*###\s'+date, line) is None and on is 1:            
                lines.append(filter_string(line))
            
            line = file.readline()



    del lines[0]
    for o in range(len(lines)):
        if lines[o]== '':
            del lines[o]
            
    print(lines)  
    return lines
