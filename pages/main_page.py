from selenium.webdriver.common.by import By
from python.pages.base_page import Page


class MainPage(Page):

    def open_main(self):
        self.open_url('https://www.amazon.com')
