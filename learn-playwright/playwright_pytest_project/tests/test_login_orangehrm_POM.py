import re
from playwright.sync_api import Page, expect
from pages.orangehrm_login_page import LoginPage
from pages.orangehrm_home_page import HomePage


def test_orangehrm(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login("Admin", "admin123")
    home_page.is_upgrade_button_visible()
    home_page.click_performance()
    home_page.click_dashboard()
