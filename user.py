from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
Options.binary_location = "C:\Program Files\Google\\Chrome\Application\chrome.exe"
webdriver_path = 'C:\\Users\\user\\Desktop\\chromedriver.exe'
options = Options()
options.add_extension("C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\cgakmbkklpmijhckpolanjijghgfpeoa\\0.1.0_0.crx")
driver = webdriver.Chrome(executable_path=webdriver_path, options=options)
driver.get("https://tw.beanfun.com/game_zone/") #前往這個網址
driver.find_element_by_id("BF_anchorLoginBtn").click()
time.sleep(3)
iframe = driver.find_elements_by_tag_name("iframe")[3]
driver.switch_to.frame(iframe)
time.sleep(1)
driver.find_element_by_id("t_AccountID").send_keys('@yahoo.com.tw')//input yours
driver.find_element_by_id("t_Password").send_keys('T')//input yours
driver.find_element_by_id("btn_login").click()

time.sleep(1)
try:
    driver.find_element_by_id("fbClose").click()
    print('ad closed')
except:
    print('no ad')
    pass

#driver.get("https://tw.beanfun.com/game_zone/")
time.sleep(1)

games=driver.find_elements_by_class_name('DetailsPanelLeft')
print(games)
driver.execute_script("arguments[0].style = 'display: block';", games[0])
games[0].find_element_by_xpath('.//input').click()
iframe = driver.find_element_by_id("fbContent")
driver.switch_to.frame(iframe)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ulServiceAccountList"]/li').click()
time.sleep(6)
driver.find_element_by_id("btnFriendlyReminderOK").click()
time.sleep(1)
pyautogui.press('left')
pyautogui.press('enter')
time.sleep(4)
#driver.quit()
