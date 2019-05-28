import requests as r
from bs4 import BeautifulSoup
import time
import threading
from datetime import date
from selenium import webdriver

chrome_path = r"C:\Users\edwardyen\Desktop\chromedriver"
web = webdriver.Chrome(chrome_path)

# open sol-idea
web.get('http://172.16.34.9')

# input account & password

account_input = web.find_element_by_xpath('//*[@id="login"]/div/form/ul/li[1]/input')
account_input.send_keys('123@123')

password_input = web.find_element_by_xpath('//*[@id="login"]/div/form/ul/li[2]/input')
password_input.send_keys('123')

login = web.find_element_by_xpath('//*[@id="login"]/div/form/div[2]/button').click()

# choose first project

web.find_element_by_xpath('//*[@id="projectArea"]/li[1]/a').click()

# ready to start

time.sleep(1)

web.find_element_by_xpath('//*[@id="link-item"]/div/a[1]').click()

time.sleep(1)

web.find_element_by_xpath('//*[@id="container"]/dl/dd/form/button').click()

time.sleep(1)

web.find_elements_by_css_selector("#gotop")[0].click()

time.sleep(1)

#######################################################################################################################

count = 0

for i in range(2, 50):
    web.find_element_by_xpath('//*[@id="link-item"]/div/a[1]').click()  ###

    time.sleep(1)

    web.find_element_by_xpath('//*[@id="container"]/dl[%i]/dd/form/button' % (i)).click()

    time.sleep(1)

    web.find_elements_by_css_selector("#gotop")[0].click()

    time.sleep(1)

    count += 1

    print('test is    ' + str(count) + '!!')