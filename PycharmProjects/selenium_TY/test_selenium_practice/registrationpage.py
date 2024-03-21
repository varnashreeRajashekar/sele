from test_selenium_practice.homepage import HomePage
from test_selenium_practice.lib1 import Wrapper, read_locators
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class RegistrationPage(HomePage):
    locators= read_locators("registration page")
    def register(self,gender,firstname,lastname, email,password):
        wrapper = Wrapper(self.driver)
        if gender == 'male':
            wrapper.click_element(self.locators["rdo_male"])
        else:
            wrapper.click_element(self.locators["rdo_female"])
        wrapper.enter_text(self.locators["txt_fname"], value=firstname)
        wrapper.enter_text(self.locators["txt_lname"], value=lastname)
        wrapper.enter_text(self.locators["txt_email"], value=email)
        wrapper.enter_text(self.locators["txt_password"], value=password)
        wrapper.enter_text(self.locators["txt_confirmpassword"], value=password)
        wrapper.click_element(self.locators["btn_register"])

        # if gender == 'male':
        #     wrapper.click_element(("id", "gender-male"))
        # else:
        #     wrapper.click_element(("id", "gender-female"))
        # wrapper.enter_text(("name", "FirstName"), value=firstname)
        # wrapper.enter_text(("id", "LastName"), value=lastname)
        # wrapper.enter_text(("id", "Email"), value=email)
        # wrapper.enter_text(("name", "Password"), value=password)
        # wrapper.enter_text(("name", "ConfirmPassword"), value=password)
        # wrapper.click_element(("name", "register-button"))

#Validating whether the user is registered or not
    def is_user_registered(self):
        for _ in range(5):
            try:
                element= self.driver.find_element("xpath",'//div[@class="result"]')
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False

