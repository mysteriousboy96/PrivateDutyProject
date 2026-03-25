# create a class
from playwright.sync_api import *


class login_page:
    def __init__(self,page:Page):
        self.page=page
        self.input_username=page.locator("//input[@id='user']")
        self.input_password = page.locator("//input[@id='pass']")
        self.chck_rememberUserId = page.locator("//input[@id='Chk_RememberMe']")
        self.chck_rememberPassword = page.locator("//input[@id='Chk_RememberPass']")
        self.btn_login = page.locator("//input[@id='btn_login']")
        self.btn_reset = page.locator("//input[@value='Reset']")
        self.link_forgotPassword = page.locator("//td[text()='Forgot Your Password?']")


    def set_username(self,username:str):
        try:
            self.input_username.clear()
            self.input_username.fill(username)
        except Exception as e:
            print(f"Error while setting username: {e}")
            raise

    def set_password(self,password:str):
        try:
            self.input_password.clear()
            self.input_password.fill(password)
        except Exception as e:
            print(f"Error while setting password: {e}")
            raise

    def click_remember_user_id(self):
        try:
            self.chck_rememberUserId.check()
        except Exception as e:
            print(f"Error while checking remember user ID: {e}")
            raise

    def click_remember_password(self):
        try:
            self.chck_rememberPassword.check()
        except Exception as e:
            print(f"Error while checking remember password: {e}")
            raise

    def click_login(self):
        try:
            self.btn_login.click()
        except Exception as e:
            print(f"Error while clicking login button: {e}")
            raise

    def click_reset(self):
        try:
            self.btn_reset.click()
        except Exception as e:
            print(f"Error while clicking reset button: {e}")
            raise

    def click_forgot_password(self):
        try:
            self.link_forgotPassword.click()
        except Exception as e:
            print(f"Error while clicking forgot password link: {e}")
            raise

    def login(self,data:dict):
        #example:
        # data = {
        #     "username": "name",
        #     "password": "pass"
        # }
        try:
            self.set_username(data["username"])
            self.set_password(data["password"])
            self.click_remember_user_id()
            self.click_remember_password()
            self.click_login()
        except Exception as e:
            print(f"Error while performing login: {e}")
            raise

    def get_homePage_title(self):
        try:
            return self.page.title()
        except Exception as e :
            print(f"Error while getting home page title: {e}")
            raise