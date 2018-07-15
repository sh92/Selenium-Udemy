from selenium import webdriver

class BrowserInteractions():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()

        driver.maximize_window()
        driver.get(baseUrl)


        title = driver.title
        print("Title of th web page is : " + title)

        currentUrl = driver.current_url
        print("Current Url of the web page is " + currentUrl)

        driver.refresh()
        print("Browser Refreshed 1st Time")

        currentUrl = driver.current_url
        print("Current Url of the web page is " + currentUrl)
        print("Browser Refreshed 2nd Time")



        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
        driver.back()
        print("Go one step back in browser history")
        currentUrl = driver.current_url
        print("Current Url of the web page is " + currentUrl)

        driver.forward()
        print("Go one step forward in browser history")
        currentUrl = driver.current_url
        print("Current Url of the web page is " + currentUrl)

        pageSource = driver.page_source
        print(pageSource)
        # driver.close()
        driver.quit()

ff = BrowserInteractions()
ff.test()