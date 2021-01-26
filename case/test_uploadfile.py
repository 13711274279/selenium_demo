import os
from log.log import Log
from commom.testng import Excel
from commom.by_element import Location
from commom.openbrowser import Browser


excel_path = os.path.dirname(os.path.dirname(__file__)) + "/excel_case/file_upload.xlsx"


class Test_Upload:

    @classmethod
    def setup(cls):
        cls.excel = Excel(excel_path)
        cls.log = Log()
        cls.log.info("Start Test_Case")
        cls.location = Location().location

    def teardown(self):
        self.log.info("End Test_Case")  # 每个用例结束执行
        self.driver.close_broswer()

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

        # 点击社保管理
        self.driver.click_element(self.location[test_data[add][2].lower()], test_data[add][3])
        add += 1

        # 点击上传社保公积金名单
        self.driver.click_element(self.location[test_data[add][2].lower()], test_data[add][3])
        add += 1

        # 上传文件
        self.driver.send_message(self.location[test_data[add][2].lower()], test_data[add][3], excel_path)
        add += 1

# if __name__ == '__main__':
#     print("开始main")
#     pytest.main(["-s", "--html=../report.html", "test_uploadfile.py"])
