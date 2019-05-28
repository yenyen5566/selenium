#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import threading
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import pandas as pd
import csv
from os import listdir
from os.path import isfile, isdir, join
from datetime import datetime, timedelta
from dateutil.parser import parse



times = int(sys.argv[1])

dir_name = sys.argv[2]


# 指定要列出所有檔案的目錄
mypath = r'C:\Users\edwardyen\PycharmProjects\selenium\測試log檔案\%s\successful'%(dir_name)

files = listdir(mypath)

name = []

final_start_time = []

final_end_time = []


#將所有資料夾名稱加入

for i in files:
    name.append(i)


csv_path = r'C:\Users\edwardyen\PycharmProjects\selenium\測試log檔案\%s\successful'%(dir_name)


#算出全部中成功的最短開始時間和最長的結束時間

for i in name:
    success_files = listdir(csv_path+'\\'+i)

    start_time = []

    end_time = []


    for k in success_files:
        with open(csv_path+'\\'+i+'\\'+k, newline='') as csvFile:

            rows = csv.DictReader(csvFile)
            for row in rows:

                start_time.append(row['2:start_time'])
                end_time.append(row['3:end_time'])

    final_start_time.append(min(start_time))
    final_end_time.append(max(end_time))


#計算出相差秒數

sec = []

for i in range(len(name)):
    a = parse(final_start_time[i])
    b = parse(final_end_time[i])

    sec.append((b-a).seconds)

#print(sec)

#加入今天日期

today = []

for i in range(len(name)):
    dat = time.strftime("%Y-%m-%d",time.localtime())
    today.append(dat)


#print(today)

#加入計算次數

ttimes = []

for i in range(len(name)):
    ttimes.append(times)

#print(ttimes)

#計算平均秒數

avg_of_time = []

for i in range(len(name)):
    avg_of_time.append(round(sec[i]/ttimes[i],4))

#print(avg_of_time)

#######################################################################################




error_path = r'C:\Users\edwardyen\PycharmProjects\selenium\測試log檔案\%s\log'%(dir_name)


final_error_times=[]

#計算錯誤次數


for e in name:

    try:
        error_counts = 0

        error_filess = listdir(error_path + '\\' + e)

        #print(error_filess)



        for k in error_filess:

            #print(e+"   "+k)

            error_times = []
            #error_add = ''
            with open(error_path + '\\' + e + '\\' + k, newline='') as csvFile:
                rows = csv.reader(csvFile)


                for row in rows:

                    if row[0] != '':
                        error_times.append(int(row[0]))
                #print(error_times)


                #print(error_times[-1])

                try:
                    if type(error_times[-1]) == int :
                        error_counts += (error_times[-1]+1)
                except:
                    error_counts += 0

                #print(error_counts)


        final_error_times.append(error_counts)

        #final_error_times.append(a)

        #print(final_error_times)

    except:
        final_error_times.append('0')
        #print('here')

#print(final_error_times)






#######################################################################################

#將以上資訊組成Dict

dict = {"1:name": name,
        "2:start_time": final_start_time,
        "3:end_time":final_end_time,
        "4:sec":sec,
        "5:times":ttimes,
        "6:avg_sec":avg_of_time,
        "7:error":final_error_times,
        "8:date":today
            }

#Dict 轉成 Dataframe

final_df = pd.DataFrame(dict)

#輸出成csv

final_df.to_csv(r'C:\Users\edwardyen\PycharmProjects\selenium\測試log檔案\%s\successful\final.csv'%(dir_name), encoding="utf-8")


#######################################################################################


error_dict = {}

for e in name:
    error_dict[e]={}

#將錯誤訊息統計


for e in name:

    try:

        #print(e)

        error_counts = 0

        error_files = listdir(error_path + '\\' + e)

        for k in error_files:

            #print(k)

            error_times = []
            with open(error_path + '\\' + e + '\\' + k, newline='') as csvFile:
                rows = csv.DictReader(csvFile)

                for row in rows:
                     if str(row['3:error_logs'])[0:100] not in error_dict[e]:

                         error_dict[e][str(row['3:error_logs'])[0:100]] =1

                     else:

                         error_dict[e][str(row['3:error_logs'])[0:100]] += 1


    except:

        pass



#print(error_dict)

error_dict = str(error_dict).replace('},','},\n')


f = open(r'C:\Users\edwardyen\PycharmProjects\selenium\測試log檔案\%s\log\log.txt'%(dir_name),'a')


f.write(str(error_dict))

f.close()


print('to_csv is finish')