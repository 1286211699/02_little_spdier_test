#coding:utf-8
import time
from selenium import webdriver
from lxml import etree
import urllib2
import random
import os
# def scroll_down(driver, sleep_pause):
#     lastHeight = driver.execute_script("return document.body.scrollHeight")
#     for i in range(0,10):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(sleep_pause)
#         newHeight = driver.execute_script("return document.body.scrollHeight")
#         if newHeight == lastHeight:
#             break
#         lastHeight = newHeight
def xunhuan():
    search_button = driver.find_elements_by_xpath('//*[@id="container"]/span[2]')[0].click()
    img_lists = driver.find_elements_by_xpath('//*[@id="srcPic"]//img')[0].get_attribute("src")
    imgs = urllib2.urlopen(urllib2.Request(url=img_lists)).read()
    time.sleep(1)
    name=img_lists[-9:-4]
    with open(name+".jpg", "wb") as f:
        f.write(imgs)
    for i in range(0, 10):
        if os.path.getsize(name+".jpg") < 100:
            print(r)
            imgs = urllib2.urlopen(urllib2.Request(url=img_lists)).read()
            with open(name+".jpg", "wb") as f:
                f.write(imgs)
            if i == 9:
                os.remove(str(r) + ".jpg")
        else:
            break
    time.sleep(1)

#代理池
proxy_list=[
    {"http":"61.135.217.7:80"},
    {"http": "101.68.73.54:53281"},
    {"http": "60.191.134.165:9999"},
    {"http": "220.249.185.178:9999"},
]
#获取浏览器控制
chromedriver = r'chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get("http://image.baidu.com/")
driver.maximize_window()
time.sleep(0.5)
search_box = driver.find_element_by_id('kw')
search_box.send_keys(u"大刀肉")
search_button = driver.find_elements_by_xpath('//*[@id="homeSearchForm"]/span[2]')[0].click()
# scroll_down(driver,0.5)
time.sleep(1)
items = driver.find_elements_by_xpath('//li[@class="imgitem"]//a')
url=items[0].get_attribute("href")
driver.get(url)
time.sleep(1)
img_list_url = driver.find_elements_by_xpath('//*[@id="srcPic"]//img')[0].get_attribute("src")
poxy=random.choice(proxy_list)
httpproxy=urllib2.ProxyHandler(poxy)
opener=urllib2.build_opener(httpproxy)
img = opener.open(urllib2.Request(url=img_list_url)).content
with open("1.jpg","wb") as f :
    f.write(img)
time.sleep(1)
for r in range(2,1001):
    try:
        try:
            xunhuan()
        except:
            xunhuan()
    except:
        xunhuan()
time.sleep(1)
driver.quit()






