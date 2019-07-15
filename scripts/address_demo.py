from Base.getdriver import get_phone_driver
from Page.Page import Page

# 手机驱动对象
drievr = get_phone_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
# 初始化Page对象
page_obj = Page(drievr)

# 点击我
page_obj.get_homepage().click_my_btn()
# 点击已有账号去登录
page_obj.get_signpage().click_exits_account()
# 登录
page_obj.get_loginpage().login("15565023683", "QQ199514")
# 点击设置按钮
page_obj.get_personpage().click_setting_btn()
# 点击地址管理
page_obj.get_settingpage().click_address_manage_btn()
# 点击新增地址
page_obj.get_address_manage_page().click_add_address_btn()
# 输入收件人
page_obj.get_add_address_page().send_recv_name("hello")
# 输入手机号
page_obj.get_add_address_page().send_recv_phone("13322221111")
# 选择所在地区
page_obj.get_add_address_page().select_ared("浙江省", "杭州市", "上城区")
# 输入详细地址
page_obj.get_add_address_page().send_detail("黑马程序员")  # ---增加中启动参数
# 输入邮编
page_obj.get_add_address_page().send_post_code("222222")
# 勾选设为默认地址
page_obj.get_add_address_page().click_default(1)
# 点击保存
page_obj.get_add_address_page().click_save_btn()
# 点击编辑按钮
page_obj.get_address_manage_page().click_edit_btn()
# 点击修改按钮
page_obj.get_address_manage_page().click_modify_btn()
# 修改用户名
page_obj.get_add_address_page().send_recv_name("world")
# 修改手机号
page_obj.get_add_address_page().send_recv_phone("13566667777")
# 修改地区
page_obj.get_add_address_page().select_ared("广东省", "东莞", "")
# 点击保存
page_obj.get_add_address_page().click_save_btn()
# 点击编辑按钮
page_obj.get_address_manage_page().click_edit_btn()
# 点击删除按钮
page_obj.get_address_manage_page().click_delete_btn()
# 点击确认删除按钮
page_obj.get_address_manage_page().click_delete_acc_dis()
