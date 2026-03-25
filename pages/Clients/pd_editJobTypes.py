from playwright.sync_api import Page


class edit_jobType:
    """
    1. Create a constructor -> add all the locators and page element inside the constructor
    make these elements as global variable by using self.
    2. Create functions for each action that you want to perform on the page.
    """

    def __init__(self,page:Page):
        self.page=page
        self.chck_allJobTypes=page.locator("//input[@id='AllJobTypes_Chk']")
        self.chck_allPrivatePay=page.locator("//td[@class='RowSubTitle2Font']/label[text()='Private Job Types']/preceding-sibling::input")
        self.chck_allInsurancePay= page.locator("//td[@class='RowSubTitle2Font']/label[text()='Insurance Job Types']/preceding-sibling::input")
        self.btn_save = page.locator("//input[@id='save_butt']")
        self.btn_close = page.locator(f"//input[@id='close']")


    def get_privatePay(self,jobType:str):
        try:
          return self.page.locator(f"//td[@id='TdClientJobtypes']/table[1]//td[@class='RowNormalFont'][contains(normalize-space(),'{jobType}')]/input[@type='checkbox']")
        except Exception as e:
            print(f"Error while getting private pay checkbox for job type '{jobType}' : {e}")
            return None

    def get_insurancePay(self,jobType:str):
        try:
            return self.page.locator(f"//td[@id='TdClientJobtypes']/table[1]//td[@class='RowNormalFont'][contains(normalize-space(),'{jobType}')]/input[@type='checkbox']")
        except Exception as e:
            print(f"Error while getting Insurance pay checkbox for job type '{jobType}' : {e}")
            return None

    def get_overrideGlobalBillRate(self,jobType:str):
        try:
            return self.page.locator(f"//td[@class='RowNormalFont'][contains(normalize-space(),'{jobType}')]/input[@type='checkbox']/parent::td/following-sibling::td[1]/input")
        except Exception as e:
            print(f"Error while getting selecting  Override Global Bill Rate checkbox for job type '{jobType}' : {e}")
            raise

    def get_clientRate(self,jobType:str):
        try:
            return  self.page.locator(f"//td[@class='RowNormalFont'][contains(normalize-space(),'{jobType}')]/input[@type='checkbox']/parent::td/following-sibling::td[2]/input")
        except Exception as e :
            print(f"Error while getting entering Client Rate for job type '{jobType}' : {e}")
            raise

    def get_overrideGlobalPayRate(self,jobType:str):
        try:
            return self.page.locator(f"//td[@class='RowNormalFont'][contains(normalize-space(),'{jobType}')]/input[@type='checkbox']/parent::td/following-sibling::td[3]/input")
        except Exception as e:
            print(f"Error while getting entering Override Global Pay Rate checkbox for job type '{jobType}' : {e}")
            raise

    def get_clientSpecificPayRate(self,jobType:str):
        try:
            return self.page.locator(f"//td[@class='RowNormalFont'][contains(normalize-space(),'{jobType}')]/input[@type='checkbox']/parent::td/following-sibling::td[4]/input")
        except Exception as e:
            print(f"Error while getting entering Client Specific Pay Rate for job type '{jobType}' : {e}")
            raise

    def get_applyBillRate(self,jobType:str):
        try:
            return self.page.locator(f"//td[@class='RowNormalFont'][contains(normalize-space(),'{jobType}')]/input[@type='checkbox']/parent::td/following-sibling::td/span[@class='applyBillRate']/input")
        except Exception as e:
            print(f"Error while getting entering Apply Bill Rate checkbox for job type '{jobType}' : {e}")
            raise

    def get_applyPayRate(self,jobType:str):
        try:
            return  self.page.locator(f"//td[@class='RowNormalFont'][contains(normalize-space(),'{jobType}')]/input[@type='checkbox']/parent::td/following-sibling::td/span[@class='applyBillRate']/input")
        except Exception as e:
            print(f"Error while getting entering Apply Pay Rate checkbox for job type '{jobType}' : {e}")
            raise


#================================================================================================================
    # Action Methods


    def click_privatePayJobType(self,jobType):
        try:
            self.get_privatePay(jobType).is_visible()
            self.get_privatePay(jobType).is_disabled()
            self.get_privatePay(jobType).click()
        except Exception as e:
            print(f"Error while getting entering Private Job Type checkbox for job type '{jobType}' : {e}")
            raise

    def click_and_set_billRate(self,jobType:str,billRate:str):
        try:
            self.get_overrideGlobalBillRate(jobType).is_visible()
            self.get_overrideGlobalBillRate(jobType).is_disabled()
            self.get_overrideGlobalBillRate(jobType).click()

            self.get_clientRate(jobType).is_visible()
            self.get_clientRate(jobType).is_enabled()
            self.get_clientRate(jobType).clear()
            self.get_clientRate(jobType).fill(billRate)
        except Exception as e:
            print(f"Error while getting entering Over Ride Bill Rate for job type '{jobType}' : {e}")
            raise






    def get_pageTitle(self):
            try:
                return self.page.title()
            except Exception as e:
                print(f"Error while getting page title: {e}")
                return None
