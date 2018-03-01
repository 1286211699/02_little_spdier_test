import pyautogui
import time
#import selenium.webdriver as webdriver


import os
import time

from selenium import webdriver

geckodriver = 'C:\Users\Administrator\Desktop\X1C-20170619\workspacePython\Save\geckodriver.exe'

os.environ["webdriver.firefox.driver"] = geckodriver

driver = webdriver.Firefox()




#driver = webdriver.Firefox()

driver.get("http://www.geetest.com/exp.html")
#driver.Manage().Window.Maximize();

driver.execute_script("window.scrollTo(0, 50);")

time.sleep(1)

#driver.maximize_window()

#driver.manage().window().maximize();

#time.sleep(1)

#pyautogui.scroll(-1)


#driver.get("http://www.163.com")


# --- #
#if addbutton.is_displayed():
#    print "addbutton displayed"
#
#

#pyautogui.moveTo(100, 100, duration=0.25)

pyautogui.moveTo(790, 1208, duration=1)
pyautogui.click(x=790, y=1208, button='left')

#pyautogui.mouseDown(x=468, y=1314, button='left')

#pyautogui.scroll(-1)

pyautogui.mouseDown()

#driver.quit()

exit(0)
