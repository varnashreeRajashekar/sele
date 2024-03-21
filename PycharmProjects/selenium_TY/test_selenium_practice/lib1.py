from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from xlrd import open_workbook
# from time import sleep

# 2.wait decorator
def wait(func):
    def _wrapper(*args,**kwargs):
        instance=args[0]
        _locator = args[1]
        print(f"waiting for {_locator}")
        w=WebDriverWait(instance.driver,20)
        w.until(visibility_of_element_located(_locator))
        return func(*args,**kwargs)
    return _wrapper

# 3.reading from excel sheet
def read_locators(sheetname):
    wb= open_workbook(r"C:\Users\DELL\Desktop\objects.xls")
    ws=wb.sheet_by_name(sheetname)
    used_rows=ws.nrows
    data={}
    for i in range(1,used_rows):
        temp_data=ws.row_values(i)
        data[temp_data[0]] = (temp_data[1],temp_data[2])
    return data

# USING CLASS DECORATOR TO READ THE DATA FROM EXCELSHEET
def attach_locators(sheetname):
    def _read_locators(cls):
        wb=open_workbook(r"C:\Users\DELL\Desktop\objects.xls")
        ws=wb.sheet_by_name(sheetname)
        used_rows=ws.nrows
        for i in range(1,used_rows):
            temp_data=ws.row_values(i)
            setattr(cls,temp_data[0],(temp_data[1],temp_data[2]))
        return cls
    return _read_locators

# Reading TEST DATA from excel
def read_headers(sheetname,scriptname):
    wb = open_workbook(r"C:\Users\DELL\Desktop\testdata.xls")
    ws = wb.sheet_by_name(sheetname)
    used_rows = ws.nrows
    for i in range(0,used_rows):
        rows =ws.row_values(i)
        if rows[0]==scriptname:
            headers= ws.row_values(i-1)
            headers=[item for item in headers if item.strip()]
            return ','.join(headers[2:])

def read_data(sheetname,scriptname):
    wb=open_workbook(r"C:\Users\DELL\Desktop\testdata.xls")
    ws=wb.sheet_by_name(sheetname)
    used_rows=ws.nrows
    final_data=[]
    for i in range(0,used_rows):
        rows=ws.row_values(i)
        if rows[0]==scriptname:
            data=[item for item in rows if item.strip()]
            if data[1]=="yes":
                final_data.append(tuple(data[2:]))
    return final_data








# 1.class
class Wrapper:
    def __init__(self,driver):
        self.driver = driver

    @wait             #click_element = wait(click_element)
    def click_element(self,locator):
        print(f"clicking on {locator}")
        self.driver.find_element(*locator).click()
        # sleep(2)
    @wait
    def enter_text(self,locator,*,value):
        print(f"clicking on {locator}")
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)
        # sleep(2)

    @wait
    def select_element(self,locator,*,value):
        element=self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_visible_text(value)

    @wait
    def mouse_hover(self,locator):
        element=self.driver.find_element(*locator)
        actions=ActionChains(self.driver)
        actions.move_to_element(element).perform()