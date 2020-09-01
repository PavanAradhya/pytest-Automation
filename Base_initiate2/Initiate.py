from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import  Config
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def startdriver():
    global driver
    if(Config.readconfig("Details","Browser")=="Chrome"):
      caps = DesiredCapabilities().CHROME
      caps['pageLoadStrategy'] = 'eager'
      path = "./Drivers/chromedriver.exe"
      driver = Chrome(executable_path=path)
      return driver

    elif (Config.readconfig("Details","Browser")=="Firefox"):
        path = "./Drivers/geckodriver.exe"
        driver = Firefox(executable_path=path)
        return driver

def closedriver():
    driver.close()
