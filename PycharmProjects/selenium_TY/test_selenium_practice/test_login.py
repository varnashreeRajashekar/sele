# 2 Creating function
# 3 create class in different file and import it here
import pytest

# from test_selenium_practice.lib1 import Wrapper, read_headers,read_data
from test_selenium_practice.conftest import reverse_
# from pytest import mark
from test_selenium_practice.loginpage import LoginPage

# headers = "email, password"
# data = [
#        ("hello.world@company.com","Password123"),
#        ("bill.gates@company.com","Password123")
#        ]
# @mark.parametrize(headers,data)
# headers=read_headers('smoke',"test_login_positive")
# data=read_data("smoke","test_login_positive")
# @mark.parametrize(headers,data)
# def test_login_positive(pages,email,password):
    # login= LoginPage(_driver)
    # login.click_login()
    # login.login(email,password)

    # pages.load()
    # pages.loginpage.click_login()
    # pages.loginpage.login(email,password)
    # #verifying whether the user is logged in or not
    # assert pages.loginpage.is_user_logged_in(email) == True
    # pages.homepage.click_logout()

    # reading data from excel
    # pages.load()
    # pages.loginpage.click_login()
    # pages.loginpage.login(email, password)
    # # verifying whether the user is logged in or not
    # assert pages.loginpage.is_user_logged_in(email) == True

    # pages.homepage.click_logout()


# data = [
#     ("hello.world@company.com", "password123"),
#     ("bill.gates@company.com", "Password12")
#       ]
# @mark.parametrize(headers,data)
# def test_login_negative(pages,email,password):
#     pages.load()
#     pages.loginpage.click_login()
#     pages.loginpage.login(email,password)
#     assert pages.loginpage.is_user_logged_in(email) == False
#     pages.loginpage.read_headers('smoke', 'test_login_negative')

    # reading data from excel
# headers=read_headers('smoke',"test_login_negative")
# data=read_data("smoke","test_login_negative")
# @mark.parametrize(headers,data)
# def test_login_negative(pages, email, password):
#     pages.load()
#     pages.loginpage.click_login()
#     pages.loginpage.login(email, password)
#     assert pages.loginpage.is_user_logged_in(email) == False
    # pages.loginpage.read_headers('smoke', 'test_login_negative')
    # pages.loginpage.read_data('smoke', 'test_login_negative')

    # ================================================================
    # wrapper= Wrapper(_driver,)
    # wrapper.click_element(("link text","Log in"))
    # wrapper.enter_text(("id", "Email"), value= email)
    # wrapper.enter_text(("id", "Password"), value= password)
    # wrapper.click_element(("xpath",'//input[@value="Log in"]'))
    # wrapper.mouse_hover(("xpath", '( //a[contains(text(),"Electronics")])[1]'))
# ============================================================================================
# STEPS TO PRODUCE

# 1.Normal selenium script-----------------

# driver.find_element("link text","Log in").click()
# sleep(2)
# driver.find_element("id", "Email").send_keys("varna1602@gmail.com")
# sleep(2)
# driver.find_element("id", "Password").send_keys("varna123")
# sleep(2)
# driver.find_element("xpath",'//input[@value="Log in"]').click()
# sleep(2)

# 2 creating function------------

# def click_element(locator_type,locator_value):
#     driver.find_element(locator_type,locator_value).click()
#
# def select_element(locator_type,locator_value,value):
#     driver.find_element(locator_type, locator_value).clear()
#     driver.find_element(locator_type,locator_value).send_keys(value)
#     sleep(2)

# 3 calling the above function---------

# click_element(("link text","Log in"))
# sleep(2)
# select_element(("id", "Email"), value="varna1602@gmail.com")
# sleep(2)
# select_element(("id", "Password"), value="varna123")
# sleep(2)
# click_element(("xpath",'//input[@value="Log in"]'))
# sleep(2)

# 4. merging the arguments and creating class-----------------

# class Wrapper:
#     def __init__(self,driver):
#         self.driver = driver
#     def click_element(self,locator):
#         print(f"clicking on {locator}")
#         self.driver.find_element(*locator).click()
#         sleep(2)
#
#     def select_element(self,locator,*,value):
#         print(f"clicking on {locator}")
#         self.driver.find_element(*locator).clear()
#         self.driver.find_element(*locator).send_keys(value)
#         sleep(2)

#5. creating object instance and calling that properties---------------

# from lib import Wrapper
# wrapper= Wrapper(driver)
#
# wrapper.click_element(("link text","Log in"))
# sleep(2)
# wrapper.select_element(("id", "Email"), value="varna1602@gmail.com")
# sleep(2)
# wrapper.select_element(("id", "Password"), value="varna123")
# sleep(2)
# wrapper.click_element(("xpath",'//input[@value="Log in"]'))
# sleep(2)


# 6. Before clicking we have to check whether the element is visible in the dom or nor. so we have to give some time
# for syncronization. for that we have decorated each function with wait function decorator.

# 7. pytest frame work
# pytest ia unit test frame work which is applied to test the python code.

# note1.--- pytest scripts file name should start with test_
# note2.--- all scripts should be under function and that function name should start with test_
# note3.--- for set up and tear down action, we create a file called conftest and move all common code present
# in all the scripts into conftest as a generator function.
# note 4.-----to get access for driver element in other scripts, we use inbuilt decorator fixture and decorate to the
# generator function and will pass that fixture name to test methods.

#
# =============================================================================================================
@pytest.fixture(name= reverse_)
def test_reverse_string(string):
    return string
print(reverse_("varna"))

