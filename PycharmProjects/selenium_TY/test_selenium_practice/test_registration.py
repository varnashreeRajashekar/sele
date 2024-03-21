from test_selenium_practice.lib1 import Wrapper, read_data,read_headers
from pytest import mark
from test_selenium_practice.registrationpage import RegistrationPage

# header="gender,firstname,lastname,email,password"
# data = [('female','varna','vikas','varna_16vik@gmail.com','Password123')]
header=read_headers("smoke","test_registration")
data=read_data("smoke","test_registration")

@mark.parametrize(header,data)
def test_registration_unique(pages,gender,firstname,lastname,email,password):
    # register= RegistrationPage(_driver)
    # register.click_register()
    # register.register(gender,firstname,lastname, email,password)

    pages.load()
    pages.registrationpage.click_register()
    pages.registrationpage.register(gender,firstname,lastname,email,password)
    #validating the registration
    assert pages.registrationpage.is_user_registered() == True

# data = [
#        ('male','varnashree','vikas','varna1603@gmail.com','123456V')]
# @mark.parametrize(header,data)
# def test_registration_duplicate(pages,gender,firstname,lastname,email,password):
#     pages.load()
#     pages.registrationpage.click_register()
#     pages.registrationpage.register(gender,firstname,lastname,email,password)
#     assert pages.registrationpage.is_user_registered() == False


