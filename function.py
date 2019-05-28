#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests as r
from bs4 import BeautifulSoup
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


def sol_idea_test(times,number):

    # record start time

    f = open ('./successful/successful_times%i.txt'%(number),'a')

    start_time = time.asctime( time.localtime(time.time()) )

    f.write('###########################################################'+'\n')

    f.write('start_time is ==============>' + start_time + '\n')

    f.close()


    #chrome_path = r"C:\Users\edwardyen\Desktop\chromedriver"
    chrome_path = "/home/azion/selenium/venv/chromedriver"
    web = webdriver.Chrome(chrome_path)

    wait = WebDriverWait(web,20)


    # open sol-idea
    #web.get('http://172.16.34.9')
    web.get('http://www.sol-idea.com.tw/')

    # input account & password

    account_input = web.find_element_by_xpath('//*[@id="login"]/div/form/ul/li[1]/input')
    #account_input.send_keys('123@123')
    account_input.send_keys('edwardyen@azion.com.tw')

    password_input = web.find_element_by_xpath('//*[@id="login"]/div/form/ul/li[2]/input')
    #password_input.send_keys('123')
    password_input.send_keys('azion123456')

    login = web.find_element_by_xpath('//*[@id="login"]/div/form/div[2]/button').click()


    # max screen

    web.maximize_window()

    # choose first project

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="projectArea"]/li[1]/a')))

    web.find_element_by_xpath('//*[@id="projectArea"]/li[1]/a').click()

    # ready to start

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="link-item"]/div/a[1]')))

    web.find_element_by_xpath('//*[@id="link-item"]/div/a[1]').click()

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/dl/dd/form/button')))

    web.find_element_by_xpath('//*[@id="container"]/dl/dd/form/button').click()

    time.sleep(1)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#gotop')))

    web.implicitly_wait(10)

    web.find_elements_by_css_selector("#gotop")[0].click()


#######################################################################################################################



    count = 0

    error_count = 0

    # start click

    for i in range(2,times+1):

        try:

            f = open('./successful/successful_times%i.txt'%number, 'a')

            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="link-item"]/div/a[1]')))

            web.find_element_by_xpath('//*[@id="link-item"]/div/a[1]').click() ###

            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/dl[%i]/dd/form/button'%(i))))

            web.find_element_by_xpath('//*[@id="container"]/dl[%i]/dd/form/button'%(i)).click()

            time.sleep(1)

            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#gotop')))

            web.implicitly_wait(10)

            web.find_elements_by_css_selector("#gotop")[0].click()



            count += 1



            print('test is ' + str(count+1) +' times !!')

            f.write('test is ==============>' + str(count+1) +' times !!'+ time.asctime( time.localtime(time.time()))+ '\n')

            f.close()


        except:

               # 如果錯誤次數小於五次,則繼續

                error_count += 1

                if error_count <= 5 :

                    l = open('./log/log%i.txt'%(number), 'a')

                    s = sys.exc_info()

                    print("Error '%s' happened on line %d    " % (s[1], s[2].tb_lineno) + time.asctime(time.localtime(time.time())) + '\n')

                    l.write("Error '%s' happened on line %d    " % (s[1], s[2].tb_lineno) + time.asctime(time.localtime(time.time())) + '\n')

                    web.quit()

                    l.close()

                    continue

                #若錯誤次數大於五次,則跳出迴圈

                else:

                    l = open('./log/log%i.txt'%(number),'a')

                    print('end time is ' + time.asctime(time.localtime(time.time())))

                    l.write('end time is ' + time.asctime(time.localtime(time.time())))

                    break

    # 全部結束,並寫下時間


    f = open('./successful/successful_times%i.txt'%(number), 'a')

    end_time = time.asctime(time.localtime(time.time()))


    f.write('finish time is ==============>'+ end_time + '\n')

    web.quit()

    f.close()




def sol_idea_test_browser(times,number):

    # record start time

    count = 0

    count_times = []

    start_readys = []

    end_readys = []

    pic_times = []

    distance_times = []

    ###################

    error_count = 0

    error_counts = []

    error_logs = []

    error_lines = []

    error_times = []



    # ready to start

    for i in range(0,times):

        try:

            time_stamp_a = time.time()

            #time_stamp_aa =time.asctime(time.localtime(time.time()))
            time_stamp_aa = time.strftime("%H:%M:%S",time.localtime())


            chrome_path = r"C:\Users\edwardyen\Desktop\chromedriver"
            #chrome_path = "/home/azion/selenium/venv/chromedriver"
            web = webdriver.Chrome(chrome_path)

            wait = WebDriverWait(web,80)

            # open sol-idea
            web.get('http://172.16.34.9')
            #web.get('http://www.sol-idea.com.tw/')

            # input account & password

            account_input = web.find_element_by_xpath('//*[@id="login"]/div/form/ul/li[1]/input')
            account_input.send_keys('123@123')
            #account_input.send_keys('edwardyen@azion.com.tw')

            password_input = web.find_element_by_xpath('//*[@id="login"]/div/form/ul/li[2]/input')
            password_input.send_keys('123')
            #password_input.send_keys('azion123456')

            login = web.find_element_by_xpath('//*[@id="login"]/div/form/div[2]/button').click()

            # max screen

            web.maximize_window()

            # choose first project

            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="projectArea"]/li[1]/a'))).click()



            #web.find_element_by_xpath('//*[@id="projectArea"]/li[1]/a')

            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="link-item"]/div/a[1]'))).click()

            #web.find_element_by_xpath('//*[@id="link-item"]/div/a[1]')

            time.sleep(1)

            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/dl/dd/form/button'))).click()

            # time sleep & implicitly_wait

            #time.sleep(1)


            pic_start = time.time()

            #web.find_element_by_xpath('//*[@id="container"]/dl/dd/form/button')


            time.sleep(3)

            #WebDriverWait(web, 80).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/dl[1]/dd/div[1]/div/a[2]'))).click()

            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/dl[1]/dd/div[1]/div/a[2]'))).click()

            pic_finish = time.time()

            pic_time = float(pic_finish - pic_start)


            web.quit()

            count += 1

            print('test is ' + str(count) + ' times !!')

            ########

            f = open('./times/times%i.txt' % (number), 'a')


            f.write('test is ==============>' + str(count) +' times !!'+ time.asctime( time.localtime(time.time()))+ '\n')

            f.close()

            ########

            time_stamp_b = time.time()

            start_readys.append(time_stamp_aa)


            #end_readys.append(time.asctime(time.localtime(time.time())))
            end_readys.append(time.strftime("%H:%M:%S",time.localtime()))

            # 計算次數並寫出


            count_times.append(str(i+1))


            pic_times.append(round(pic_time,4))

            distance_times.append(round((time_stamp_b - time_stamp_a),4))



        except:

            error_count +=1

            # 當錯誤次數小於五次,則繼續

            if error_count <= 10:

                s = sys.exc_info()

                print("Error '%s' happened on line %d    " % (s[1], s[2].tb_lineno) + time.asctime(time.localtime(time.time())) + '\n')

                error_counts.append(str(i+1))

                error_logs.append(s[1])

                error_lines.append(s[2].tb_lineno)

                #error_times.append(time.asctime(time.localtime(time.time())))
                error_times.append(time.strftime("%H:%M:%S",time.localtime()))

                web.quit()

                continue

            else:
                # 若大於五次則跳出迴圈



                #print('end time is ' + time.asctime(time.localtime(time.time())))
                print('end time is ' + time.strftime("%H:%M:%S",time.localtime()))
                break


    dict = {"1:number": count_times,
            "2:start_time": start_readys,
            "3:end_time":end_readys,
            "4:pic_times":pic_times,
            "5:total_time":distance_times
            }

    successful_df = pd.DataFrame(dict)


    dict_error = {"1:number":error_counts,
                  "2:error_lines":error_lines,
                  "3:error_logs":error_logs,
                  "4:error_time":error_times

    }


    error_df = pd.DataFrame(dict_error)

    successful_df.to_csv("./successful/successful%i.csv"%(number), encoding="utf-8")

    error_df.to_csv("./log/error_log%i.csv"%(number), encoding="utf-8")

    #print(successful_df)

    #print(error_df)

    # 全部結束,並寫下時間


    #end_time = time.asctime(time.localtime(time.time()))

    end_time = time.strftime("%H:%M:%S",time.localtime())

    print('finish time is ==============>'+ end_time + '\n')


#############################################################################################


