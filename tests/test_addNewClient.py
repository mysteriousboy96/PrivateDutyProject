import pytest
from pages.loginPage import *
from utils.data_reader_utli import *
from config import Config
from pages.navigationMenu_SubMenu import *
from pages.Clients.pd_addNewClient import *

json_data=read_json_data("C:/Pycharm/PythonProject/PythonProject1/PDProjectWithFW/testdata/logindata.json")
data = read_json_data("C:/Pycharm/PythonProject/PythonProject1/PDProjectWithFW/testdata/ClientData.json")



@pytest.mark.parametrize("test_data", json_data, ids=[f"{d['username']}-{d['expected']}" for d in json_data])
def test_addClient(page,test_data):



    # create a object for the class which we want to use
    loginPage = login_page(page)
    navPath = navigation(page)
    newClient = addNewClient(page)



    #======login to the application===========
    loginPage.login(test_data)

    if test_data['expected']=='success':
        expect(page).to_have_title(loginPage.get_homePage_title())
    else:
        print(f"Login failed for user: {test_data['username']} with expected result: {test_data['expected']}")


    navPath.click_menu("Clients->New Client")
    newClient.addNewClient(data)
















