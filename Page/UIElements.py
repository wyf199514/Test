from selenium.webdriver.common.by import By


class UIElements:
    """管理所有页面元素"""

    """首页"""
    # 首页我的按钮
    home_my_btn_id = (By.ID, "com.yunmall.lc:id/tab_me")

    """注册页面"""
    # 已有账号去登录
    sign_exits_account_btn_id = (By.ID, "com.yunmall.lc:id/textView1")

    """登录页面"""
    # 用户名
    login_account_id = (By.ID, "com.yunmall.lc:id/logon_account_textview")
    # 密码
    login_passwd_id = (By.ID, "com.yunmall.lc:id/logon_password_textview")
    # 登录按钮
    login_btn_id = (By.ID, "com.yunmall.lc:id/logon_button")
    # 关闭登录页面按钮
    login_close_page_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

    """个人中心页面"""
    # 我的优惠券
    person_shop_cart_id = (By.ID, "com.yunmall.lc:id/txt_my_coupons")
    # 设置按钮
    person_setting_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

    """设置页面"""
    # 退出按钮
    setting_logout_btn_id = (By.ID, "com.yunmall.lc:id/setting_logout")
    # 弹窗 确认退出按钮
    setting_acc_quit_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")
    # 弹窗 取消退出按钮
    setting_dis_quit_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_left_button")
    # 地址管理按钮
    address_manage_btn_id = (By.ID, "com.yunmall.lc:id/setting_address_manage")
    """设置 - 地址管理页面"""
    # 返回按钮
    address_manage_return_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")
    # 编辑按钮
    address_manage_edit_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_right_btn")
    # 新增地址按钮
    address_manage_add_address_btn_id = (By.ID, "com.yunmall.lc:id/address_add_new_btn")
    # 收件人和手机号
    address_manage_rec_phone_text_id = (By.ID, "com.yunmall.lc:id/receipt_name")
    # 默认
    address_manage_default_text_id = (By.ID, "com.yunmall.lc:id/address_is_default")
    # 地址
    address_manage_address_text_id = (By.ID, "com.yunmall.lc:id/receipt_address")
    # 修改按钮
    address_manage_modify_btn_id = (By.ID, "com.yunmall.lc:id/modify")
    # 删除按钮
    address_manage_delete_btn_id = (By.ID, "com.yunmall.lc:id/delete")
    # 确认删除按钮
    address_manage_acc_delete_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_left_button")
    # 取消删除按钮
    address_manage_dis_delete_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")


    """设置 - 地址管理 - 新增地址页面"""
    # 新增地址页面返回按钮
    new_address_return_btn_id = (By.ID, "com.yunmall.lc:id/back")
    # 保存按钮
    new_address_save_btn_id = (By.ID, "com.yunmall.lc:id/button_send")
    # 收件人
    new_address_recv_name_id = (By.ID, "com.yunmall.lc:id/address_receipt_name")
    # 手机号
    new_address_recv_phone_id = (By.ID, "com.yunmall.lc:id/address_add_phone")
    # 详细地址
    new_address_recv_detail_id = (By.ID, "com.yunmall.lc:id/address_detail_addr_info")
    # 邮编
    new_address_post_code_id = (By.ID, "com.yunmall.lc:id/address_post_code")
    # 设为默认地址
    new_address_default_btn_id = (By.ID, "com.yunmall.lc:id/address_default")
    # 所在地区 -选择按钮
    new_address_select_area_btn_id = (By.ID, "com.yunmall.lc:id/address_province")
    # 所在地区 -选择省
    new_address_select_sheng_btn_xpath = (By.XPATH, "//*[contains(@text,'%s')]")
    # 所在地区 -选择市
    new_address_select_shi_btn_xpath = (By.XPATH, "//*[contains(@text,'%s')]")
    # 所在地区 -选择区
    new_address_select_qu_btn_xpath = (By.XPATH, "//*[contains(@text,'%s')]")

