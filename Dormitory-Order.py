from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def OpenUrl():
    # 访问网址
    driver.get(url)

def Login():
    # 查询登录按钮
    #driver.find_element_by_id("login_submit").click()
    #time.sleep(1)
    # 输入账号
    print( driver.find_element_by_id("username"))
    driver.find_element_by_id("username").send_keys(Name)
    # 输入密码
    print(driver.find_element_by_id("password"))
    driver.find_element_by_id("password").send_keys(Password)
    time.sleep(2)
    # 点击登录按钮
    driver.find_element_by_id("login_submit").click()
    time.sleep(2)

def change():
    But_update=driver.find_element_by_id("But_update").click()
    while(True):
        select_39403()
        select_39407()
        select_39411()
        select_39412()
        select_39415()
        select_39416()


    #T_ssbz=driver.find_element_by_id("T_ssbz").click()
    #T_ssbz = driver.find_element_by_("39412").click()
def select_39403():
        select_button = Select(driver.find_element_by_id('T_ssbz'))  # 实例化Select
        select_button.select_by_value("39403")
        driver.find_element_by_id("IBut_qd").click()
        driver.switch_to.alert.accept()
        time.sleep(0.1)
def select_39407():
    select_button = Select(driver.find_element_by_id('T_ssbz'))  # 实例化Select
    select_button.select_by_value("39407")
    driver.find_element_by_id("IBut_qd").click()
    driver.switch_to.alert.accept()
    time.sleep(0.1)

def select_39411():
    select_button = Select(driver.find_element_by_id('T_ssbz'))  # 实例化Select
    select_button.select_by_value("39411")
    driver.find_element_by_id("IBut_qd").click()
    driver.switch_to.alert.accept()
    time.sleep(0.1)



def select_39412():
    select_button = Select(driver.find_element_by_id('T_ssbz'))  # 实例化Select
    select_button.select_by_value("39412")
    driver.find_element_by_id("IBut_qd").click()
    driver.switch_to.alert.accept()
    time.sleep(0.1)


def select_39415():
    select_button = Select(driver.find_element_by_id('T_ssbz'))  # 实例化Select
    select_button.select_by_value("39415")
    driver.find_element_by_id("IBut_qd").click()
    driver.switch_to.alert.accept()
    time.sleep(0.1)


def select_39416():
    select_button = Select(driver.find_element_by_id('T_ssbz'))  # 实例化Select
    select_button.select_by_value("39416")
    driver.find_element_by_id("IBut_qd").click()
    driver.switch_to.alert.accept()
    time.sleep(0.1)
if __name__ == "__main__":
    # 打开谷歌浏览器
    option = webdriver.ChromeOptions()

    # option.add_argument('headless')
    #browser = webdriver.Chrome(options=option)
    Name = input("输入认证用户名: ")
    Password = input("输入认证密码: ")
    headless = int(input("是否打开浏览器?0代表后台打开浏览器，1代表前台打开浏览器: "))
    if headless == 0:
        option.add_argument("--headless")
    # option.add_argument("–window-size=10,10")
    option.add_argument("start-maximized")
    option.add_argument("enable-automation")
    # option.add_argument("--headless")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-infobars")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--disable-browser-side-navigation")
    option.add_argument("--disable-gpu")
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=option)
    url = "https://ca.csu.edu.cn/authserver/login?service=http%3a%2f%2fnewcomer.its.csu.edu.cn%2fsso.aspx"
    OpenUrl()
    Login()
    url="http://newcomer.its.csu.edu.cn/NewSchoolSystemYJS/W_ss_ydss.aspx"
    OpenUrl()
    change()
    #driver.quit()