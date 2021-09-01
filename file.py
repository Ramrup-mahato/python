import csv
#import pandas as pd
#import numpy as np
from datetime import date, datetime, time
from os import read

dates = []
emp = []
with open('Employee_Checkin.csv', 'r') as file:
    reader = csv.reader(file)
    column = next(reader)
    for i in reader:
        if i[6]!='Time' and datetime.strptime(i[6],"%Y-%m-%d %H:%M:%S").date() not in dates:
            dates.append(datetime.strptime(i[6],"%Y-%m-%d %H:%M:%S").date())

with open('Employee_Checkin.csv', 'r') as file:
    reader = csv.reader(file)
    columns = next(reader)
    for dat in sorted(dates):
        details = {}
        # print(next(reader))
        for row in reader:
            if dat != datetime.strptime(row[6],"%Y-%m-%d %H:%M:%S").date():continue
            if row[1] in details:
                details[row[1]][row[5]] = row[6]
                ot = datetime.strptime(details[row[1]]['OUT'],"%Y-%m-%d %H:%M:%S")-datetime.strptime(details[row[1]]['IN'],"%Y-%m-%d %H:%M:%S")
                if round(ot.total_seconds()/3600,1) > 8:
                     details[row[1]]['OT'] = round(ot.total_seconds()/3600,1)-8
                else:
                     details[row[1]]['OT'] = 0
                em = [i for i in details[row[1]].values()]
                em.insert(0, row[1])
                emp.append(em)
            else:
                di = {
                    row[5] : row[6]
                }
                details[row[1]] = di
#print (emp)
    #print(emp)
csv_columns = ['employe','OUT','IN','OT']
#csv_file = "Rahuls.csv"
with open('file.csv', 'w', newline='') as f:
   
    writer = csv.writer(f)
    writer.writerow(csv_columns)
    for data in emp:
            writer.writerow(data)
    #writer.writerow(emp)

    


#wr = csv.writer(f,quoting=csv.QUOTE_ALL)
