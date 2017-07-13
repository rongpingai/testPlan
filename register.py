# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
    
driver.get('http://test.liangdawang.com:8085/portal/page/register/register.html')
driver.find_element_by_class_name("green").click()

driver.find_element_by_xpath("//*[@id='fxsmContent']").send_keys(Keys.DOWN)
time.sleep(3)

driver.find_element_by_xpath("//*[@id='go_fxsm']").click()
