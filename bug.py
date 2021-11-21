from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import requests 
import os
useremail='b10909029@gapps.ntust.edu.tw'
password='qweewwioppoo'
login_url='https://www.instagram.com/'

browser=webdriver.Chrome( )

url='https://www.instagram.com/'

def tt():
    browser.get(url)
    WebDriverWait(browser,30).until(EC.presence_of_element_located((By.NAME,'username')))
    user_input=browser.find_elements_by_name('username')[0]
    password_input=browser.find_elements_by_name('password')[0]
    user_input.send_keys(useremail)
    password_input.send_keys(password)

    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,
    '//*[@id="loginForm"]/div/div[3]/button')))
    login_click = browser.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]/button')[0]
    login_click.click()

    WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button')))
    later_click=browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')[0]
    later_click.click()

    WebDriverWait(browser,50).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')))
    notify_later=browser.find_elements_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')[0]
    notify_later.click()
tt()
time.sleep(3)
browser.get("https://www.instagram.com/drunk_santa_2021/")
time.sleep(0.5)
WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')))
browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')[0].click()
time.sleep(3)
index=0
q=1
for i in range(1,35):
    q=1500*i
    js='document.getElementsByClassName("isgrP")[0].scrollTop='+str(q)
    browser.execute_script(js)
    time.sleep(1.5)


all=browser.find_elements_by_class_name('_6q-tv')
#all=browser.find_elements_by_css_selector('div div div div ul div li div div div div a img')
#all=browser.find_elements_by_css_selector('li div div div div a img'or'li div div div div span img')
list=[]  
del all[0]   
del all[0]
for element in all:
    img=element.get_attribute('src')
    list.append(img)
for link in list:
    img=requests.get(link)  
    index=index+1  
    with open("images\\"  + str(index) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
        file.write(img.content) 
    