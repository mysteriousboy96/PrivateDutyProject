from playwright.sync_api import Page
from .pd_editJobTypes import *

class addNewClient:

    def __init__(self,page:Page):

        self.page=page
        self.editJobType=edit_jobType(page)

        #locators
        # input fields for adding new client
        self.input_firstName=page.locator("//input[@id='firstName']")
        self.input_lastName=page.locator("//input[@id='lastName']")
        self.input_middleName=page.locator("//input[@id='middleName']")
        self.input_address1=page.locator("//textarea[@id='address1']")
        self.input_address2=page.locator("//textarea[@id='address2']")
        self.input_city=page.locator("//input[@id='city']")
        self.input_state=page.locator("//input[@id='state']")
        self.input_zipcode=page.locator("//input[@id='zip']")
        self.input_email=page.locator("//input[@id='emailTxt']")
        self.input_homePhone=page.locator("//input[@id='clientPhone']")
        self.input_workPhone=page.locator("//input[@id='clientWorkPhone']")
        self.input_cellPhone=page.locator("//input[@id='clientCell']")

        #buttons
        self.btn_jobTypeSelect=page.locator("//input[@id='btnRegister']")
        self.btn_continue = page.locator("//input[@id='Continue_Buttn']")
        self.btn_cancel = page.locator("//input[@id='Cancel_Buttn']")


        #links
        self.link_referredBy=page.locator("//td[@class='RowNormalFont']/b/a")

        #dropdowns
        self.dpdn_salutation = page.locator("//select[@id='salutation_DD']")

 #========================================================================================#
        #functions --> Action Methods

    def set_firstName(self,firstName:str):
        try:
            self.input_firstName.clear()
            self.input_firstName.fill(firstName)
        except Exception as e:
            print(f"Error while setting first name: {e}")
            raise

    def set_middleName(self,middleName:str):
        try:
            self.input_middleName.clear()
            self.input_middleName.fill(middleName)
        except Exception as e:
            print(f"Error while setting middle name: {e}")
            raise


    def set_lastName(self,lastName:str):
        try:
            self.input_lastName.clear()
            self.input_lastName.fill(lastName)
        except Exception as e:
            print(f"Error while setting last name: {e}")
            raise

    def set_address1(self,address1:str):
        try:
            self.input_address1.clear()
            self.input_address1.fill(address1)
        except Exception:
            print(f"Error while setting Address1: {Exception}")
            raise

    def set_address2(self,address2:str):
        try:
            self.input_address2.clear()
            self.input_address2.fill(address2)
        except Exception:
            print(f"Error while setting Address2: {Exception}")
            raise

    def set_city(self,city:str):
        try:
            self.input_city.clear()
            self.input_city.fill(city)
        except Exception:
            print(f"Error while setting City: {Exception}")
            raise

    def set_state(self, state: str):
        try:
            self.input_state.clear()
            self.input_state.fill(state)
        except Exception:
            print(f"Error while setting State: {Exception}")
            raise

    def set_zip(self, state: str):
        try:
            self.input_state.clear()
            self.input_state.fill(state)
        except Exception:
            print(f"Error while setting Zip: {Exception}")
            raise

    def set_email(self, email: str):
        try:
            self.input_email.clear()
            self.input_email.fill(email)
        except Exception:
            print(f"Error while setting Email: {Exception}")
            raise

    def set_homePhone(self, homePhone: str):
        try:
            self.input_homePhone.clear()
            self.input_homePhone.fill(homePhone)
        except Exception:
            print(f"Error while setting Home Phone: {Exception}")
            raise


    def set_workPhone(self, workPhone: str):
        try:
            self.input_workPhone.clear()
            self.input_workPhone.fill(workPhone)
        except Exception:
            print(f"Error while setting Work Phone: {Exception}")
            raise

    def set_cell(self, cell: str):
        try:
            self.input_cellPhone.clear()
            self.input_cellPhone.fill(cell)
        except Exception:
            print(f"Error while setting cell : {Exception}")
            raise


    def addNewClient(self,data:dict):
        try:
            self.set_firstName(data['firstName'])
            self.set_middleName(data['middleName'])
            self.set_lastName(data['lastName'])
            self.set_address1(data['address1'])
            self.set_address2(data['address2'])
            self.set_city(data['city'])
            self.set_state(data['state'])
            self.set_zip(data['zip'])
            self.set_email(data['email'])
            self.set_homePhone(data['homePhone'])
            self.set_workPhone(data['workPhone'])
            self.set_cell(data['cellPhone'])
            self.click_jobType()
            self.editJobType.click_privatePayJobType(data['jobType'])
            self.editJobType.click_and_set_billRate(data['jobType'],data['billRate'])

        except Exception as e:
            print(f"Error while adding new client: {e}")
            raise

    def click_jobType(self):
        try:
            self.btn_jobTypeSelect.click()
        except Exception as e:
            print(f"Error while clicking job type select button: {e}")
            raise