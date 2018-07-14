from selenium import webdriver

class FindByIdName():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")

        if elementById is not None:
            print("We foudn an element by Id")

        elementByname = driver.find_element_by_name("show-hide")

        if elementByname is not None:
            print("We found an element by Name")


ff = FindByIdName()
ff.test()
