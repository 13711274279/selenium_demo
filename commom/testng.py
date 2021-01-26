import random
from log.log import Log
from commom.areacode import regional_code
import requests
import re
import pandas
import xlrd
from xlutils.copy import copy


class PhoneNum:
    def __init__(self):
        self.log = Log()

    def phone(self):  # 生成一个电话号码
        __choise = range(0, 10)
        __ra = random.sample(__choise, 8)
        __second = random.choice([5, 3, 8, 7])
        __thrid = random.choice([6, 7, 5, 9])
        __phone_number = '1%s%s' % (__second, __thrid) + ''.join(str(i) for i in __ra)
        self.log.info("号码：{}".format(__phone_number))
        return __phone_number

    def batch_phone(self, num):  # 随机生成指定的号码
        __phone = []
        while True:
            if len(sorted(set(__phone))) < num:
                __phone.append(self.phone())
            else:
                if len(__phone) != num:
                    for item in range(len(__phone) - num):
                        __phone.pop(num - item)
                break
        print(len(__phone))
        return __phone


class ID:
    def __init__(self):
        self.log = Log()

    """
        循环的次数，每次循环都生成100条数据
    """

    def get_id(self, num):
        self.__code = None
        self.id_codelist = []
        for item in regional_code:
            self.__code = tuple(item[86].keys())
        for item in range(num):
            year = random.randint(1980, 1996)
            month = random.randint(1, 12)
            day = random.randint(1, 30)
            rank_code = [item for item in regional_code[0][self.__code[random.randint(1, len(self.__code) - 1)]]]
            result = requests.get(
                url='http://sfz.uzuzuz.com/?region={code}&birthday={day}&sex={sex}&num=100&r={endnum}'.
                    format(code=rank_code[random.randint(1, len(rank_code) - 1)],
                           day=str(year) + str(month).zfill(2) + str(day).zfill(2),
                           sex=random.randint(1, 2),
                           endnum=random.randint(1, 99))
            )
            parrent = re.compile('<td style="vertical-align: middle;">(.*)</td>')
            one = parrent.findall(result.text)
            list2 = sorted(set(one), key=one.index)
            for item in list2:
                self.id_codelist.append(item)
        self.log.info("身份证{}".format(self.id_codelist))
        return self.id_codelist


class TestData:
    def __init__(self):
        from faker import Faker
        self.faker = Faker(locale='zh_CN')

    def names(self):  # 姓名
        return self.faker.name() + str(random.randint(1, 10000))

    def address(self):  # 地址
        return self.faker.address()

    def ean(self, length):  # EAN条形码
        return self.faker.ean(length)

    def feture_datatime(self, day):  # 未来日期 格式YYYY-MM-DD  HH-MM-SS
        return self.faker.future_datetime(end_date="+{}d".format(day), tzinfo=None)

    def future_date(self, day):  # 未来日期 格式YYYY-MM-DD
        return self.faker.future_date(end_date="+{}d".format(day), tzinfo=None)

    def past_datetime(self, day):  # 过去日期 格式YYYY-MM-DD  HH-MM-SS
        return self.faker.past_datetime(start_date="-{}d".format(day), tzinfo=None)

    def past_date(self, day):  # 过去日期 格式YYYY-MM-DD
        return self.faker.past_date(start_date="-{}d".format(day), tzinfo=None)

    def ssn(self, num, min_age, max_age, ):  # 身份证生成
        if num == 1:
            return self.faker.ssn(min_age=min_age, max_age=max_age)
        else:
            id_list = []
            while True:
                if len(sorted(set(id_list))) < num:
                    id_list.append(self.faker.ssn(min_age=min_age, max_age=max_age))
                else:
                    if len(id_list) != num:
                        for item in range(len(id_list) - num):
                            id_list.pop(num - item)
                    break
            return id_list

    def md5(self):  # 随机生成MD5
        return self.faker.md5()

    def uuid(self):  # 随机UUID
        return self.faker.uuid4()

    def text(self):  # 随机生成一小段文章
        return self.faker.text()


class Excel:
    def __init__(self, path):
        self.path = path
        self.pd = pandas
        self.df = self.pd.read_excel(self.path)
        self.write = xlrd
        self.workbook = xlrd.open_workbook(self.path)
        self.sheets = self.workbook.sheet_names()
        self.worksheet = self.workbook.sheet_by_name(self.sheets[0])
        # 获取行
        self.rows_old = self.worksheet.nrows
        # 获取列
        self.cols_old = self.worksheet.ncols

    def read(self, num=None):  # 读取EXCEL返回列表
        if num is None:
            return self.df.values
        else:
            return self.df.values[num]

    def wirteResult(self, num, data, result):  # 写入结果
        new_workbook = copy(self.workbook)
        new_worksheet = new_workbook.get_sheet(0)
        values = self.read()
        length = len(values[0])
        if values[num - 1][-1] == "T":
            print(num + 1, print(len(values) - 3))
            new_worksheet.write(num, length - 3, data)
            new_worksheet.write(num, length - 2, result)
        if values[num - 1][-1] == 'F':
            if result == 'fail':
                new_worksheet.write(num, length - 3, data)
                new_worksheet.write(num, length - 2, result)
        new_workbook.save(self.path)

    def reassert(self, data, response):
        newline = []
        for item in data:
            if item == "[" or item == "]":
                string = '\\' + item
                newline.append(string)
            elif item == "{" or item == "}":
                string = "\\" + item
                newline.append(string)
            elif item == '(' or item == ')':
                string = "\\" + item
                newline.append(string)
            else:
                newline.append(item)
        data = "".join(newline)
        contrast = re.compile(data)
        answer = contrast.findall(response)
        return data, answer
