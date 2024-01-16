import re

import file as fi
#filename='E:/vscode_file/vscode_file/markdown/英语学习/词汇记录.md'


class month:
    def __init__(self,name,days_num) -> None:
        self.name=name
        self.days=[]
        self.days_num=days_num
class year:
    def __init__(self,name,months_num) -> None:
        self.months=[]
        self.name=name
        self.months_num=months_num



def filter_string(text,content):             #过滤text内容
    filtered_text=re.sub(content,"",text)                #过滤任意长度数字
    filtered_text=re.sub(r'\n',"",filtered_text)         #过滤掉\n
    return filtered_text

def get_date_content():            #获取目录，返回years
    
    years=[]
    num_year=0
    num_month=0
    num_day=0
    
    
    print(fi.filename)
    with open(fi.filename, 'r',encoding=fi.get_file_encoding(fi.filename)) as file:
        line = file.readline()
        
        while line:
            if re.match('#\s', line):
                years.append(year(filter_string(line,'# '),0))
                num_year=num_year+1
                num_month=0
                num_day=0
            elif  re.match('##\s', line):
                years[num_year-1].months.append(month(filter_string(line,'## '),0))
                num_month+=1
                years[num_year-1].months_num=num_month
                num_day=0
            elif  re.match('###\s', line):
                years[num_year-1].months[num_month-1].days.append(filter_string(line,'### '))
                num_day+=1
                years[num_year-1].months[num_month-1].days_num=num_day
            
            line = file.readline() 
    return years
