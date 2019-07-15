from Base.Base import Base
from Page.UIElements import UIElements


class AddressManage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_return_btn(self):
        """点击返回按钮"""
        self.click_element(UIElements.address_manage_return_btn_id)

    def click_edit_btn(self):
        """点击编辑按钮"""
        self.click_element(UIElements.address_manage_edit_btn_id)

    def click_add_address_btn(self):
        """点击新增地址按钮"""
        self.click_element(UIElements.address_manage_add_address_btn_id)

    def get_address_detail(self):
        """获取地址详细信息"""
        # 取收件人和手机号
        recv_name_phone = self.get_element(UIElements.address_manage_rec_phone_text_id).text
        # 取默认
        default = self.get_element(UIElements.address_manage_default_text_id).text
        # 取所在地区
        area = self.get_element(UIElements.address_manage_address_text_id).text

        return {"name_phone": recv_name_phone, "default": default, "area": area}

    def click_modify_btn(self):
        """点击修改按钮"""
        self.click_element(UIElements.address_manage_modify_btn_id)

    def click_delete_btn(self):
        """点击删除按钮"""
        self.click_element(UIElements.address_manage_delete_btn_id)

    def click_delete_acc_dis(self, tag=1):
        """
        删除弹窗确认和取消按钮
        :param tag: 1：删除 其他值取消
        :return:
        """
        if tag == 1:
            self.click_element(UIElements.address_manage_acc_delete_btn_id)
        else:
            self.click_element(UIElements.address_manage_dis_delete_btn_id)
