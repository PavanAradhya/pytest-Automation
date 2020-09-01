from Library import Config
from selenium.webdriver.support.select import Select
class register:
    def __init__(self,obj):
        global driver
        driver = obj
    def GetURL(self, URL):
        driver.get(Config.readconfig("Details", "URL"))
        driver.maximize_window()

    def Username(self,Username):
        driver.find_element_by_xpath(Config.elementLoc("RegElements", "Username")).send_keys(Username)

    def EmailID(self, EmailID):
        driver.find_element_by_xpath(Config.elementLoc("RegElements", "EmailID")).send_keys(EmailID)

    def Passward(self, Passward):
        driver.find_element_by_xpath(Config.elementLoc("RegElements", "Passward")).send_keys(Passward)

    def Cpassward(self, Cpassward):
        driver.find_element_by_xpath(Config.elementLoc("RegElements", "Cpassward")).send_keys(Cpassward)

    def DOB(self, DOB):
        driver.find_element_by_xpath(Config.elementLoc("RegElements", "DOB")).send_keys(DOB)

    def Phone(self, Phone):
        driver.find_element_by_xpath(Config.elementLoc("RegElements", "Phone")).send_keys(Phone)

    def Home(self, Home):
        driver.find_element_by_xpath(Config.elementLoc("RegElements", "Home")).click()
    def Scroll(self,Scroll):
        driver.execute_script(Config.elementLoc("RegElements", "Scroll"))

    def Sex(self,Sex):
        obj = Select(driver.find_element_by_xpath(Config.elementLoc("RegElements", "Sex")))
        obj.select_by_index(1)


    def Country(self,Country):
        obj = Select(driver.find_element_by_xpath(Config.elementLoc("RegElements", "Country")))
        obj.select_by_visible_text("India")


    def State(self,State):
        obj = Select(driver.find_element_by_xpath(Config.elementLoc("RegElements", "State")))
        obj.select_by_visible_text("Karnataka")


    def City(self,City):
        obj = Select(driver.find_element_by_xpath(Config.elementLoc("RegElements", "City")))
        obj.select_by_visible_text("Ranibennur")


    def Zip(self,Zip):
        driver.find_element_by_xpath(Config.elementLoc("RegElements", "Zip")).send_keys("581115")

    def Terms(self,Terms):
        driver.find_element_by_xpath(Config.elementLoc("RegElements", "Terms")).click()

    def SignUp(self,SignUp):
        driver.find_element_by_xpath(Config.elementLoc("RegElements", "SignUp")).click()

    def Login(self,Login):
        driver.find_element_by_xpath(Config.elementLoc("RegElements", "Login")).click()

    def Username2(self,Username2):
        driver.find_element_by_xpath(Config.elementLoc("RegElements", "Username2")).send_keys(Username2)

    def Passward2(self,Passward2):
        driver.find_element_by_xpath(Config.elementLoc("RegElements", "Passward2")).send_keys(Passward2)

    def Login2(self,Login2):
        driver.find_element_by_xpath(Config.elementLoc("RegElements", "Login2")).click()
