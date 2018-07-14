from selenium import webdriver
import os

class RunChromeTest():
    def test(self):
        driverLocation = "/Users/withgod/Documents/lib/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # instantiate FF browser command
        driver = webdriver.Chrome(driverLocation)
        # Open the provided URL
        driver.get("http://www.letskodeit.com")

ff = RunChromeTest()
ff.test()