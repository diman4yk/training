from selenium.webdriver.remote.webelement import WebElement

from base.seleniumbase import SeleniumBase
from base.utils import Utils


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '#menu-main>li'
        self.NAV_LINK_TEXT = 'КАТАЛОГ,ДОСТАВКА И ОПЛАТА,ОБМЕН И ВОЗВРАТ,ОТЗЫВЫ,КОНТАКТЫ'

    def get_nav_links(self):
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_strings(nav_links_text)

    def get_nav_link_by_name(self, name) -> WebElement:
        elements = self.get_nav_links()
        return self.get_element_by_text(elements, name)
