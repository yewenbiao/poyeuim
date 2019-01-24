# 快速复制  ctrl + d   删除 ctrl + y
from selenium.webdriver.common.by import By

# app信息
# setting
setting_appPackage = "com.android.settings"
setting_appActivity = ".Settings"

# sms配置
sms_appPackage = 'com.android.mms'
sms_appActivity = '.ui.ConversationList'

# 开发者头条配置
toutiao_appPackage = 'io.manong.developerdaily'
toutiao_appActivity = 'io.toutiao.android.ui.activity.MainActivity'

# =========================================================================

#开发者头条
home_page_textview_my =(By.XPATH,"//*[contains(@text,'我的') and contains(@resource-id,'io.manong.developerdaily:id/tv_tab_title')]")
#点击登录按钮 "io.manong.developerdaily:id/login_btn"
home_page_btn_login = (By.ID, "io.manong.developerdaily:id/login_btn")
#==========login_pgae===========
# 4.使用邮箱登录注册# driver.find_element_by_id("io.manong.developerdaily:id/btn_email")
login_page_btn_email = (By.ID,"io.manong.developerdaily:id/btn_email")
# 5.输入邮箱# email =  driver.find_element_by_id("io.manong.developerdaily:id/edt_email")
login_page_edit_email = (By.ID,"io.manong.developerdaily:id/edt_email")
# 6.输入密码# pwd = driver.find_element_by_id("io.manong.developerdaily:id/edt_password")
login_page_edit_pwd = (By.ID,"io.manong.developerdaily:id/edt_password")
# 7.点击登录# driver.find_element_by_id("io.manong.developerdaily:id/btn_login").click()
login_page_btn_email_login = (By.ID,"io.manong.developerdaily:id/btn_login")
#登录后用户id  io.manong.developerdaily:id/nav_tv_name
login_page_textview_loginuser = (By.ID,"io.manong.developerdaily:id/btn_login")
#昨日收益
login_page_textview_yesterday_earnings = (By.Id,"io.manong.developerdaily:id/nav_btn_coin_yesterday")
#职业规划
login_page_textview_career_planning = (By.ID,"io.manong.developerdaily:id/nav_btn_ucp")

# setting_search_page
setting_page_btn_search = (By.ID,"com.android.settings:id/search")
setting_page_edit_search_content = (By.ID,"android:id/search_src_text")

# display_page
display_page_textview_show = (By.XPATH, "//*[contains(@text,'显示')]")
display_page_btn_search = (By.ID, "com.android.settings:id/search")
display_page_edit_search_content = (By.ID, "android:id/search_src_text")
display_page_btn_back = (By.CLASS_NAME, "android.widget.ImageButton")

# network_page
network_page_textview_more = (By.XPATH, "//*[contains(@text,'更多')]")
network_page_textview_mobile_network = (By.XPATH, "//*[contains(@text,'移动网络')]")
network_page_textview_first_network = (By.XPATH, "//*[contains(@text,'首选网络')]")
network_page_textview_2g = (By.XPATH, "//*[contains(@text,'2G')]")
network_page_textview_3g = (By.XPATH, "//*[contains(@text,'3G')]")

# home_page


# sms_page
sms_page_btn_add_sms = (By.ID, "com.android.mms:id/action_compose_new")
sms_page_edit_recipient = (By.ID, "com.android.mms:id/recipients_editor")
sms_page_edit_sms_content = (By.ID, "com.android.mms:id/embedded_text_editor")
sms_page_btn_send_sms = (By.ID, "com.android.mms:id/send_button_sms")
sms_page_textview_sms_contents = (By.ID, "com.android.mms:id/text_view")

# 分类


# 购物车
