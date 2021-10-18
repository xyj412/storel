from selenium import webdriver

import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get(r"http://8.129.91.152:8765/")

driver.find_element_by_xpath("//*[@class='no-border special-color']").click()

driver.find_element_by_xpath("//input[@name='phone']").send_keys("15894567941")

time.sleep(10)

driver.find_element_by_xpath("//a[@class='btn btn-success left reget-mobileCode']").click()

time.sleep(1)

text = driver.find_element_by_xpath("//*[@class='layui-layer-content']")
str = text.text
aaa = str[len(str)-4:]

driver.find_element_by_xpath('//*[@name="code"]').send_keys(aaa)

driver.find_element_by_xpath("//input[@name='password']").send_keys("qwer123456")

driver.find_element_by_xpath("//input[@name='agree']").click()

driver.find_element_by_xpath("//*[@class='btn btn-special']").click()

time.sleep(0.3)

driver.find_element_by_xpath("//a[@class='layui-layer-btn1']").click()

time.sleep(5)

driver.find_element_by_xpath("//*[@src='/Public/frontend/images/personal_center/identity_iden_no.png' and @title='实名认证']").click()

time.sleep(2)

driver.find_element_by_xpath("//*[@class='link-color fs-12 right realname-check']").click()

time.sleep(1)

driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/form/div[1]/div/input').send_keys("张三")

driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/form/div[2]/div/input').send_keys("341114199007300000")

driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/form/div[3]/div/button').click()






