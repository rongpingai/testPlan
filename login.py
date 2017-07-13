# coding = utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
    
driver.get('http://test.liangdawang.com:8085/portal/page/login/login.html')
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("ld_wl001")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("loginButtn").click()

driver.find_element_by_class_name("signout").click()