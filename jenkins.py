from selenium import webdriver
from time import sleep

username = input('username:')
password = input('password:')

try:
    pts = webdriver.ChromeOptions()
    pts.binary_location = ("D:/Program Files/Google/Chrome/Application/chrome.exe")
    driver = webdriver.Chrome(chrome_options=pts, executable_path="D:/selenium_test/chromedriver.exe")
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.find_element_by_id('loginStoreId').send_keys(username)
    sleep(3)
    driver.find_element_by_xpath("//input[@id='loginUserPwd1']").click()
    sleep(3)
    driver.find_element_by_xpath("//input[@id='loginUserPwd']").send_keys(password)
    sleep(3)
    driver.find_element_by_class_name('qd_btn').click()
    driver.implicitly_wait(10)
    print('pass')
    driver.quit()
except Exception:
    driver.quit()
    print('error')
