from selenium import webdriver

class FindByClassName():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementByClassName = driver.find_element_by_class_name("displayed-class")

        if elementByClassName is not None:
            print("We foudn an element by Class Name")

        elementByTagName = driver.find_element_by_tag_name("a")

        if elementByTagName is not None:
            print("We found an element by Tage Name")


ff = FindByClassName()
ff.test()
