from selenium import webdriver
import os

class RunFFTests():
    def test(self):
        # instantiate FF browser command
        driver = webdriver.Firefox()
        # Open the provided URL
        driver.get("http://www.letskodeit.com")

ff = RunFFTests()
ff.test()