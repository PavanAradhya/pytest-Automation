from Base_initiate2 import Initiate
from selenium.webdriver.support.select import Select
from Library import Config
from Pages import Registration
from DataGenerator import DataSet
import pytest
import time

@pytest.fixture()
def start():
    global driver
    driver = Initiate.startdriver()
    driver.get(Config.readconfig('Details', 'URL'))
    driver.maximize_window()
    yield
    driver = Initiate.closedriver()

def test_register(start):
    reg = Registration.register(driver)
    reg.Username("pavan@gmail.com")
    reg.EmailID("pavan@gmail.com")
    reg.Passward("Pavan@123")
    reg.Cpassward("Pavan@123")
    reg.DOB("09/04/1992")
    reg.Phone("8976113456")
    reg.Home("Home")
    time.sleep(3)
    reg.Scroll("Scroll")
    reg.Sex("Sex")
    time.sleep(5)
    reg.Country("Country")
    time.sleep(5)
    reg.State("State")
    time.sleep(5)
    reg.City("City")
    time.sleep(5)
    reg.Zip("Zip")
    reg.Terms("Terms")
    reg.SignUp("SignUp")
    time.sleep(5)

def test_signup(start):
    reg = Registration.register(driver)
    reg.Login("Login")
    time.sleep(5)
    reg.Username2("Username2")
    reg.Passward2("Passward2")
    reg.Login2("Login2")
    time.sleep(5)
    assert driver.current_url=="https://www.thetestingworld.com/testings/dashboard.php"

@pytest.mark.parametrize('data',DataSet.datagen())
def test_dataset(data):
    driver = Initiate.startdriver()
    driver.get(Config.readconfig("Details", "URL"))
    driver.maximize_window()
    reg = Registration.register(driver)
    reg.Login("Login")
    time.sleep(5)
    reg.Username2(data[0])
    reg.Passward2(data[1])
    reg.Login2("Login2")







