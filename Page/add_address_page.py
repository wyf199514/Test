from Base.Base import Base
from Page.UIElements import UIElements


class AddAddressPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def send_recv_name(self, name):
        """收件人"""
        self.send_element(UIElements.new_address_recv_name_id, name)

    def send_recv_phone(self, phone):
        """手机号"""
        self.send_element(UIElements.new_address_recv_phone_id, phone)

    def select_ared(self, sheng, shi, qu):
        """所在地区"""
        # 点击选择按钮
        self.click_element(UIElements.new_address_select_area_btn_id)
        # 选择省
        self.click_element((UIElements.new_address_select_sheng_btn_xpath[0],
                            UIElements.new_address_select_sheng_btn_xpath[1] % sheng))
        # 选择市
        self.click_element(
            (UIElements.new_address_select_shi_btn_xpath[0], UIElements.new_address_select_shi_btn_xpath[1] % shi))
        if qu:
            # 选择区
            self.click_element(
                (UIElements.new_address_select_qu_btn_xpath[0], UIElements.new_address_select_qu_btn_xpath[1] % qu))

    def send_detail(self, detail):
        """详细地址"""
        self.send_element(UIElements.new_address_recv_detail_id, detail)

    def send_post_code(self, code):
        """邮编"""
        self.send_element(UIElements.new_address_post_code_id, code)

    def click_default(self, is_default):
        """
        设为默认地址
        :param is_default: 如果不为空，执行点击操作，由数据文件控制
        :return:
        """
        if is_default:
            self.click_element(UIElements.new_address_default_btn_id)

    def click_return_btn(self):
        """点击返回按钮"""
        self.click_element(UIElements.new_address_return_btn_id)

    def click_save_btn(self):
        """保存按钮"""
        self.click_element(UIElements.new_address_save_btn_id)
