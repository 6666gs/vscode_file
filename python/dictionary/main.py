import dictionary as dic

date='23/12/14'
date.replace('/','\/')

content=dic.read_from_date(date)

for i in range(len(content)):
    print(dic.get_CN(content[i]))
    