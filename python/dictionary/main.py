import dictionary as dic

date='24/1/9'

content=dic.read_from_date(date)

for i in range(len(content)):
    print(dic.get_CN(content[i]))
    