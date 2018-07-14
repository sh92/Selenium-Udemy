from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByClassName():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementById = driver.find_element(By.ID, "name")
        if elementById is not None:
            print("We found an element by Id")

        elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        if elementByXpath is not None:
            print("We foud an element by Xpath")


        elementByLinkText = driver.find_element(By.LINK_TEXT, "Login")
        if elementByLinkText is not None:
            print("We foud an element by Link Text")


ff = FindByClassName()
ff.test()
