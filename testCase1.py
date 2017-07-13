# coding = utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)

driver.find_element_by_xpath("//*[@id='page']/a[10]").send_keys(Keys.DOWN)
time.sleep(2)
driver.find_element_by_xpath("//*[@id='s_tab']/a[9]").send_keys(Keys.UP)
time.sleep(2)
driver.find_element_by_xpath("//*[@id='con-ar']/div[3]/a").send_keys(Keys.DOWN)