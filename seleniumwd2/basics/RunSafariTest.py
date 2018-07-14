from selenium import webdriver
import os

class RunSafariTest():
    def test(self):
        serverLocation = "/Users/withgod/Documents/lib/selenium-server-standalone-3.13.0.jar"
        os.environ["SELENIUM_SERVER_JAR"] = serverLocation
        # instantiate FF browser command
        driver = webdriver.Safari()
        # Open the provided URL
        driver.get("http://www.letskodeit.com")

ff = RunSafariTest()
ff.test()