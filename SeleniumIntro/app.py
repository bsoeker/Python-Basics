from selenium import webdriver


def launchBrowser():
    options = webdriver.ChromeOptions()
    options.add_argument(argument="start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver


driver = launchBrowser()
