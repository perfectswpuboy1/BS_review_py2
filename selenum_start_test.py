#coding:utf-8
#!/usr/bin/env python
# encoding=utf-8
#from selenium import webdriver
#from selenium import webdriver
#browser = webdriver.Chrome()
#browser.get('http://www.baidu.com/')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print driver.page_source