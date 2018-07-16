from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GetText():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        openTablElement = driver.find_element(By.ID, "opentab")
        elementText = openTablElement.text
        print("Text on element is : " + elementText)
        time.sleep(1)
        driver.quit()

ff = GetText()
ff.test()