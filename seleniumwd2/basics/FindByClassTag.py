from selenium import webdriver

class FindByClassName():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementByClassName = driver.find_element_by_class_name("inputs displayed-class")
        elementByClassName.send_keys("Testing The Element")

        if elementByClassName is not None:
            print("We foudn an element by Class Name")

        elementByTagName = driver.find_element_by_tag_name("a")
        elementByTagName.send_keys("Testing The Element")

        if elementByTagName is not None:
            print("We found an element by Tage Name")


ff = FindByClassName()
ff.test()
