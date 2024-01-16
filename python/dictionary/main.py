from colorama import init,Fore
import os

import dictionary as dic
import date as da
import file as fi

'''
发现如果from file import filename时
filename只能读取使用，无法修改
import file后才可以
'''

init(autoreset=True)    #字体颜色初始化



while True:
    
    file_exist=fi.file_check();
    print(file_exist)
    if file_exist==1:
        
        fi.update_filename(os.path.join(os.path.dirname(__file__),'英语单词记录.md'))
    elif isinstance(file_exist,str):
        fi.update_filename(file_exist)
    else:
        print('单词记录文件缺失！！\n请补充单词文件绝对路径\n')
        new_dir=input('单词文件绝对路径：')
        word_file_name=os.path.join(os.path.dirname(__file__),'单词路径.txt')
        with open(word_file_name, 'w',encoding='GBK') as file:
            file.write(new_dir)
        fi.update_filename(new_dir)     #更新全局变量
        if os.path.exists(fi.filename):
            pass
        else:
            print('文件路径不合法，请重新输入！')
            continue
    
    
    years=da.get_date_content()
    num=len(years)
    os.system('cls')
    print('*'*30)
    print('*'*30+'\n')
    print(Fore.BLUE+' '*7+'单词记录查询系统\n')
    print('*'*30)
    print('*'*30)
    print('\n'+'='*30)
    print('年份如下：')
    print('='*30)
    for i in range(len(years)):
        print(Fore.GREEN + years[i].name)
    print('='*30)
    year=input('请输入要查询的年份:(按下q以退出)\n')
    if year == 'q':
        break
    else:
        i=0
        while i<num:
            if year == years[i].name:
                index_year=i
                break
            i+=1
        if i ==num:
            input('未找到目标年份，按下enter返回。。。\n')
        else:
            while True:
                os.system('cls')
                months=years[index_year].months
                num=years[index_year].months_num
                print('*'*30)
                print('*'*30+'\n')
                print(Fore.BLUE+' '*7+'单词记录查询系统\n')
                print('*'*30)
                print('*'*30)
                print('\n'+'='*30)
                print('目标年份：'+year)
                print('月份如下：')
                print('='*30)
                for i in range(num):
                    print(Fore.GREEN + months[i].name)
                print('='*30)
                month=input('请输入要查询的月份:(只输入月)(按下q以退出)\n')
                if month =='q':
                    break
                else:
                    month=years[index_year].name+'/'+month
                    i=0
                    while i<num:
                        if month == months[i].name:
                            index_month=i
                            break
                        i+=1
                    if i ==num:
                        input('未找到目标月份，按下enter返回。。。')
                    else:
                        while True:
                            os.system('cls')
                            days=months[index_month].days
                            num=months[index_month].days_num
                            print('*'*30)
                            print('*'*30+'\n')
                            print(Fore.BLUE+' '*7+'单词记录查询系统\n')
                            print('*'*30)
                            print('*'*30)
                            print('\n'+'='*30)
                            print('目标月份：'+month)
                            print('日期如下：')
                            print('='*30)
                            for i in range(num):
                                print(Fore.GREEN + days[i])
                            print('='*30)
                            day=input('请输入要查询的日期:(只输入天)(按下q以退出)\n')
                            if day =='q':
                                break
                            else:
                                day=months[index_month].name+'/'+day
                                i=0
                                while i<num:
                                    if day == days[i]:
                                        index_day=i
                                        break
                                    i+=1
                                if i ==num:
                                    input('未找到目标日期，按下enter返回。。。')
                                else:
                                    content_word=dic.read_from_date(day)
                                    print('='*30)
                                    print('\n')
                                    for i in range(len(content_word)):
                                        dic_temp=dic.get_CN(content_word[i])
                                        if isinstance(dic_temp,str):
                                            print(Fore.GREEN + dic_temp,end='')
                                        else:
                                            print(Fore.GREEN + dic_temp[0],end='')
                                            print(' '*(25-len(dic_temp[0])),end='')
                                            io=2
                                            
                                            while io<len(dic_temp):
                                                print(Fore.BLUE + dic_temp[io],end='')
                                                io=io+1
                                                if io >=len(dic_temp):
                                                    break
                                                print('\n',end='')
                                                print(' '*25,end='')
                                        print('\n',end='')
                                    input('按下enter以返回。。。')
                        
    
    
        
    