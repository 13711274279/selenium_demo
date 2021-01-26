import os
from log.log import Log
from commom.testng import Excel
from commom.by_element import Location
from commom.openbrowser import Browser

BASE_DIR = os.path.split(os.path.abspath(__file__))[0]
excel_path = "/webdriver/excel_case/add_employee.xlsx"


class Test_AddEmeployee:

    @classmethod
    def setup(cls):
        cls.excel = Excel(excel_path)
        cls.log = Log()
        cls.log.info("Start Test_Case")
        cls.location = Location().location

    def teardown(self):
        self.driver.close_broswer() # 关闭浏览器
        self.log.info("End Test_Case")  # 每个用例结束执行

    def test_addemployyed(self):
        self.driver = Browser()
        test_data = self.excel.read()
        add = 0
        self.driver.open_windows("http://hrmtestt.bndxqc.com/login")

        # 输入账号
        self.driver.send_message(self.location[test_data[add][2].lower()], test_data[add][3], int(test_data[add][4]))
        add += 1

        # 输入密码
        self.driver.send_message(self.location[test_data[add][2].lower()], test_data[add][3], int(test_data[add][4]))
        add += 1

        self.driver.click_element(self.location[test_data[add][2].lower()], test_data[add][3])  # 点击登录
        add += 1

        self.driver.click_element(self.location[test_data[add][2].lower()], test_data[add][3])  # 点击人事管理
        add += 1

        self.driver.click_element(self.location[test_data[add][2].lower()], test_data[add][3])  # 点击员工管理
        add += 1

        self.driver.click_element(self.location[test_data[add][2].lower()], test_data[add][3])  # 点击新增员工
        add += 1

        self.driver.click_element(self.location[test_data[add][2].lower()], test_data[add][3])  # 国籍
        add += 1

# if __name__ == '__main__':
#     print("开始main")
#     pytest.main(["-s",  "--html=../report.html","test_addemeployee.py"])
