from Page.homepage import HomePage
from Page.signpage import SignPage
from Page.loginpage import LoginPage
from Page.personpage import PersonPage
from Page.settingpage import SettingPage
from Page.address_manage_page import AddressManage
from Page.add_address_page import AddAddressPage
import time
class Page:

    def __init__(self, driver):
        self.driver = driver

    def get_homepage(self):
        """返回首页实例化对象"""
        return HomePage(self.driver)

    def get_signpage(self):
        """返回注册页面实例化对象"""
        return SignPage(self.driver)

    def get_loginpage(self):
        """返回登录页面对象"""
        return LoginPage(self.driver)

    def get_personpage(self):
        """返回个人中心页面对象"""
        return PersonPage(self.driver)

    def get_settingpage(self):
        """返回设置页面对象"""
        return SettingPage(self.driver)

    def get_address_manage_page(self):
        """返回地址管理页面对象"""
        return AddressManage(self.driver)

    def get_add_address_page(self):
        """返回新增地址页面对象"""
        return AddAddressPage(self.driver)
