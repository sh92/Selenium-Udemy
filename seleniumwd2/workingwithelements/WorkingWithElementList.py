from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementList():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)


        radioButtonlist = driver.find_elements(By.XPATH, "//input[contains(@type, 'radio') and contains(@name,'cars')]")
        size = len(radioButtonlist)
        print("Size of the list: "+ str(size))

        for radioButton in radioButtonlist:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)


ff = WorkingWithElementList()
ff.test()