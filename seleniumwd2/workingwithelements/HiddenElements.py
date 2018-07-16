from selenium import webdriver
import time


class HiddenElements():

    def testletsKodeIt(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        textBoxElement = driver.find_element_by_id("displayed-text")
        textBoxState = textBoxElement.is_displayed() # True if visible, False if hidden
        # Exception if not present in the DOM
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)

        driver.find_element_by_id("hide-textbox").click()

        textBoxElement = driver.find_element_by_id("displayed-text")
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)



        driver.find_element_by_id("show-textbox").click()
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)
        driver.quit()

ff = HiddenElements()
ff.testletsKodeIt()