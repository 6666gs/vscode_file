import requests
from bs4 import BeautifulSoup
import re

import file as fi
#filename='E:/vscode_file/vscode_file/markdown/英语学习/词汇记录.md'
'''
得到word的含义
首先搜索单词含义
其次搜索短语
最后搜索网络翻译

若都无，则输出未找到

输出格式：列表：[word,含义的数量,含义1,含义2,...]
'''
def get_CN(word):                    #返回的dic为列表[word,音标数量,(音标1),(音标2),含义的数量,含义1,含义2,...]
    root_url = 'https://www.youdao.com/result?word='
    url = root_url +  word + '&lang=en' # 拼接URL
    response = requests.get(url)
    dic=[word]
    # 检查请求是否成功
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')
        target_element = soup.find('div', class_='phone_con')
        if target_element:
            
            meanings = target_element.find_all('div',class_='per-phone')
            if meanings:
                for i in range(len(meanings)):
                    dic.append(meanings[i].get_text())     
                    
                dic.insert(1,i+1)
                num_pre=len(dic)
            else:
                dic.append(0)  
                num_pre=len(dic)
        else:
            dic.append(0)  
            num_pre=len(dic)
        
        #搜索单词释义
        target_element = soup.find('ul', class_='basic')
        if target_element:
            
            meanings = target_element.find_all(class_='word-exp')
            
            if meanings:
                for i in range(len(meanings)):
                    dic.append(meanings[i].get_text())     
                    
                dic.insert(num_pre,i+1)
                return dic   #返回的dic为列表[word,音标数量,(音标1),(音标2),含义的数量,含义1,含义2,...]
            
                
        else:
            #未找到直接相关的单词，开始搜索短语
            target_element = soup.find('div', class_='webPhrase')
            if target_element:
                meanings = target_element.find_all('li',class_='mcols-layout')
                
                for i in range(len(meanings)):
                    dic.append(filter_string(meanings[i].get_text()))     
                    
                dic.insert(num_pre,i+1)
                return dic
            else:
                #未找到短语，搜寻网络翻译结果
                target_element = soup.find('p', class_='trans-content')
                if target_element:
                    
                    dic.append(filter_string(target_element.get_text()))         
                    dic.insert(num_pre,1)
                    return dic
                else:
                    return '######未找到单词或短语或网络释义：'+word
    else:
        print('请求失败，状态码:', response.status_code)
    
    
def filter_string(text):             #过滤text内容
    filtered_text=re.sub('\d*',"",text)                  #过滤任意长度数字
    filtered_text=re.sub('\s*\.\s*',"",filtered_text)    #过滤任意长度空格+.+任意长度空格
    filtered_text=filtered_text.strip()
    filtered_text=re.sub(r'\n',"",filtered_text)         #过滤掉\n
    #filtered_text=re.sub('\s',"",text)
    return filtered_text

def read_from_date(date):            #获取date日期中的单词名单，输出为列表，date为具体到某一天
    
    date.replace('/','\/')
    lines=[1]
    with open(fi.filename, 'r',encoding=fi.get_file_encoding(fi.filename)) as file:
        line = file.readline()
        on=0
        while line:
            #匹配到对应日期
            if re.match('###\s'+date, line) and on == 0:
                on=1
            #匹配到下一个日期或者分割横线
            elif  (re.match('###\s', line) or re.match('##\s', line) or re.match('#\s', line) or re.match('---', line) )  and on == 1:
                on=0
                break
            
            if re.match('###\s'+date, line) is None and on == 1:            
                lines.append(filter_string(line))      
            
            line = file.readline()
    del lines[0]
    lines=[i for i in lines if i!='']   #列表推导式太优雅了 桀桀桀
    return lines


get_CN('analogously')