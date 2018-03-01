import pyautogui
import os
import time

from selenium import webdriver

chromedriver = r'D:\diver.exe\chromedriver.exe'

#os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)

#driver = webdriver.Chrome()



driver.get("http://www.geetest.com/exp.html")

time.sleep(1)

print driver.get_window_position()
#driver.get("http://www.163.com")

driver.maximize_window()

driver.execute_script("window.scrollTo(0, 300)")
time.sleep(1)

exit(0)

x = 890
y = 270

#GUI Graphical User Interface

#Automachine Automobile Automatic

pyautogui.moveTo(x, y, duration=1)
pyautogui.click(x=x, y=y, button='left')

pyautogui.mouseDown()

exit(0)
