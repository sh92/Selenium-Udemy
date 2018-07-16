from selenium import webdriver
from selenium.webdriver.common.by import By
from  utilities.handy_wrapper import HandyWrappers
import time

class UsingWrappers():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        textField1 = hw.getElement("name")
        textField1.send_keys("Test")
        time.sleep(2)

        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()


ff = UsingWrappers()
ff.test()