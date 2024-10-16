from pages.main_page import MainPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"
login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    login_page.should_be_register_form()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()