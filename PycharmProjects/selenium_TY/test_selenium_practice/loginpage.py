from test_selenium_practice.lib1 import Wrapper
from test_selenium_practice.lib1 import attach_locators
from test_selenium_practice.homepage import HomePage
from selenium.common.exceptions import NoSuchElementException
from time import sleep

@attach_locators("loginpage")
class LoginPage(HomePage):
    # locators=read_locators("loginpage")
        # locators={ "txt_email" : ("name", "Email"), "txt_password" : ("id","Password"),
        #        "btn_login":("xpath", '//input[@value="Log in"]')}
    def login(self,email,password):

        # excel function----------
        # wrapper=Wrapper(self.driver)
        # wrapper.enter_text(self.locators["txt_email"],value = email)
        # wrapper.enter_text(self.locators["txt_password"], value = password)
        # wrapper.click_element(self.locators["btn_login"])

        # excel decorator----------------
        wrapper = Wrapper(self.driver)
        wrapper.enter_text(self.txt_email, value=email)
        wrapper.enter_text(self.txt_password, value=password)
        wrapper.click_element(self.btn_login)

        # VALIDATION--validating the data------------------------ validation func should be written in POM classes but actual
        # validation should be done in test scripts
    def is_user_logged_in(self,email):
        for _ in range(5):
            try:
                element= self.driver.find_element( "xpath" , f'// a[text() = "{email}"]')  #--------since it is
       # dynamic x-path, we will not read it from excel and we will write it in the from generic function.
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False


# without reading from excel file----------------

        # wrapper.enter_text(("id", "Email"), value=email)
        # wrapper.enter_text(("id", "Password"), value=password)
        # wrapper.click_element(("xpath", '//input[@value="Log in"]'))


