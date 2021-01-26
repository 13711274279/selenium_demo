import logging
from logging import handlers
from configparser import ConfigParser
import datetime
import os

inipath = os.path.dirname(os.path.dirname(__file__)) + '/config.ini'
BASE_DIR = os.path.split(os.path.abspath(__file__))[0]
log_file = os.path.join(BASE_DIR) + '//log_file//'



class Log:
    def __init__(self, fmt='%(asctime)s %(funcName)s:{long}%(message)s'.format(long=" " * 2)):
        self.cf = ConfigParser()
        self.cf.read(inipath, encoding='utf-8')
        self.logpath = self.cf.get('mylog', 'log')
        self.logger = logging.getLogger(__name__)
        self.format_str = logging.Formatter(fmt)
        self.logger.setLevel(level=logging.DEBUG)
        self.logfile = handlers.TimedRotatingFileHandler(
            filename=log_file + '{:%Y%m%d}.log'.format(datetime.date.today()),
            when='D', backupCount=10, encoding='utf-8')
        self.logfile.setFormatter(self.format_str)
        if not self.logger.handlers:  # 这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
            self.logger.addHandler(self.logfile)
            self.controler = logging.StreamHandler()
            self.controler.setFormatter(self.format_str)
            self.logger.addHandler(self.controler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)
        return self.logger

    def warning(self, msg):
        self.logger.warning(msg)
        return self.logger

    def error(self, msg):
        self.logger.error(msg)
        return self.logger
