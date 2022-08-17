from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import json

def OpenUrl():
    # 访问网址
    driver.get(url)

def Login():
    # 查询登录按钮
    #driver.find_element(value="login_submit").click()
    #time.sleep(1)

    # 输入账号
    driver.find_element(value="username").send_keys(Name)
    # 输入密码
    driver.find_element(value="password").send_keys(Password)

    driver.find_element(value="rememberMe").click()

    # 点击登录按钮
    driver.find_element(value="login_submit").click()
    time.sleep(0.5)

# def saveCookies():
#     cookies = driver.get_cookies()    # 获取cookies
#     f1 = open('cookie.txt', 'w')    #cookies存入文件JSON字符串
#     f1.write(json.dumps(cookies))
#     f1.close()

# #未成功
# def readCookies():
#     try:
#         driver.set_page_load_timeout(2)
#         # 设置cookies前必须访问一次登录的页面
#         driver.get(url)
#     except:
#         driver.set_page_load_timeout(10)
#         with open("cookie.txt", "r") as fp:
#             cookies = json.load(fp)
#             for cookie in cookies:
#                 cookie.pop('domain')  # 如果报domain无效的错误
#                 driver.add_cookie(cookie)

#         driver.get("http://newcomer.its.csu.edu.cn/sso.aspx")
#         #driver.refresh()

def select_39403():
    select_button = Select(driver.find_element(value='T_ssbz'))  # 实例化Select
    select_button.select_by_value("39403")
    driver.find_element(value="IBut_qd").click()
    driver.switch_to.alert.accept()
    time.sleep(0.5)

def select_39405():
    select_button = Select(driver.find_element(value='T_ssbz'))  # 实例化Select
    select_button.select_by_value("39405")
    driver.find_element(value="IBut_qd").click()
    driver.switch_to.alert.accept()
    time.sleep(0.5)

def select_39407():
    select_button = Select(driver.find_element(value='T_ssbz'))  # 实例化Select
    select_button.select_by_value("39407")
    driver.find_element(value="IBut_qd").click()
    driver.switch_to.alert.accept()
    time.sleep(0.5)

def select_39411():
    select_button = Select(driver.find_element(value='T_ssbz'))  # 实例化Select
    select_button.select_by_value("39411")
    driver.find_element(value="IBut_qd").click()
    driver.switch_to.alert.accept()
    time.sleep(0.5)

def select_39412():
    select_button = Select(driver.find_element(value='T_ssbz'))  # 实例化Select
    select_button.select_by_value("39412")
    driver.find_element(value="IBut_qd").click()
    driver.switch_to.alert.accept()
    time.sleep(0.5)

def select_39415():
    select_button = Select(driver.find_element(value='T_ssbz'))  # 实例化Select
    select_button.select_by_value("39415")
    driver.find_element(value="IBut_qd").click()
    driver.switch_to.alert.accept()
    time.sleep(0.5)

def select_39416():
    select_button = Select(driver.find_element(value='T_ssbz'))  # 实例化Select
    select_button.select_by_value("39416")
    driver.find_element(value="IBut_qd").click()
    driver.switch_to.alert.accept()
    time.sleep(0.5)

def change():
    while(True):
        time.sleep(0.5)
        url="http://newcomer.its.csu.edu.cn/NewSchoolSystemYJS/W_ss_ydss.aspx"
        OpenUrl()
        try:
            But_update=driver.find_element(value="But_update").click()
        except:
            print("未找到update")
            pass

        try:
            #1200，4人间，有独卫和阳台
            select_39412()
        except:
            print("选择1200 4人间失败")
            pass

        try:
            #1200，二室一厅，有独卫
            select_39415()
        except:
            print("选择1200 二室一厅失败")
            pass

        try:
            #1200，三室两厅，有卫生间和阳台
            select_39416()
        except:
            print("选择1200 三室两厅失败")
            pass

        try:
            #1000，4人间，有独卫，无阳台
            select_39407()
            #600，4人间，上床下桌，无独卫和阳台
            select_39403()
            # #1000，6人间，有卫生间，无阳台
            # select_39411()
            # #600，6人间，无独卫和阳台
            # select_39405()
        except:
            print("其他宿舍选择失败")
            pass

if __name__ == "__main__":

    # 打开谷歌浏览器
    option = webdriver.ChromeOptions()
    
    Name = input("输入认证用户名: ")
    Password = input("输入认证密码: ")
    headless = int(input("是否打开浏览器?0代表后台打开浏览器，1代表前台打开浏览器: "))
    
    if headless == 0:
        option.add_argument("--headless")
    
    # option.add_argument("–window-size=10,10")
    option.add_argument("start-maximized")
    option.add_argument("enable-automation")

    option.add_argument("--no-sandbox")
    option.add_argument("--disable-infobars")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--disable-browser-side-navigation")
    option.add_argument("--disable-gpu")
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    # option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=option)

    url = "https://ca.csu.edu.cn/authserver/login?service=http%3a%2f%2fnewcomer.its.csu.edu.cn%2fsso.aspx"
    # url="http://newcomer.its.csu.edu.cn/sso.aspx"
    OpenUrl()
    Login()
    #readCookies()

    url="http://newcomer.its.csu.edu.cn/NewSchoolSystemYJS/W_ss_ydss.aspx"
    OpenUrl()
    change()

    #driver.quit()