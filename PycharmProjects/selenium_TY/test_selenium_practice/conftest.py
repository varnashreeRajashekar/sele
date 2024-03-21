from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from pytest import fixture
from test_selenium_practice.loginpage import LoginPage
from test_selenium_practice.homepage import HomePage
from test_selenium_practice.registrationpage import RegistrationPage
from selenium import webdriver

# HOOK FUNCTION
# this is a hook function, where it will be executed before other test methods and we can take command line arguements.
# pytest_addoption should be the name of the hook function.
# parser is the inbuilt fixture.
# parser.addoption--------- parser may be the class name and addoption is the function in that class. so we are calling
# that function by using class name

# allowed_environments=("test", "stage")
# allowed_browsers=("chrome", "firefox","edge","safari")
# def pytest_addoption(parser):
#     parser.addoption("--env", action="store",dest="env",default="test",choices=allowed_environments)
#     parser.addoption("--browser",action="store", dest="browser" , default="chrome", choices=allowed_browsers)
#
# # request is a inbuilt fixture used to read the data from above fixture.
# @fixture
# def _driver(request):
#     browser_type=request.config.option.browser.capitalize()
#     driver=getattr(webdriver,browser_type)()
#     yield driver
#     driver.close()

    # driver= Chrome()
    # yield driverg
    # driver.close()

'''TO MAINTAIN ALL TEST ENVIRONMENT CONFIGUARTIONS'''
# class TestConfigurations:
#     url='https://demowebshop.tricentis.com/'
#     email="hello.world@company.com"
#     password="Password123"
#
# class StageConfigurations:
#     url = 'https://demowebshop.tricentis.com/'
#     email = "bill.gates@company.com"
#     password = "Password123"
#
# @fixture
# def config(request):
#     execution_env=request.config.option.env
#     if execution_env.upper() == "TEST":
#         return TestConfigurations
#     elif execution_env.upper() == "STAGE":
#         return StageConfigurations
#     else:
#         raise Exception("unknown congiguration")
#
#     # if env =="test":
#     #     return TestConfigurations()
#     # elif env == "stage":
#     #     return StageConfigurations()
#     # else:
#     #     raise Exception("unknown configuration")
# @fixture
# def pages(_driver,config):
#     class Pages:
#         loginpage = LoginPage(_driver)
#         registrationpage = RegistrationPage(_driver)
#         homepage = HomePage(_driver)
#
#         def load(self):
#             _driver.maximize_window()
#             _driver.get(config.url)
#
#     return Pages()


def reverse_(string):
    return string[::-1]
