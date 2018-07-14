from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElement():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementListbyClassName = driver.find_elements_by_class_name("inputs")
        length = len(elementListbyClassName)

        if elementListbyClassName is not None:
            print("ClassName -> Size of the list is: "+str(length))

        elementListByTagName = driver.find_elements(By.TAG_NAME,"td")
        length2 = len(elementListByTagName)

        if elementListByTagName is not None:
            print("TagName -> Size of the list is: "+ str(length2))


ff = ListOfElement()
ff.test()
