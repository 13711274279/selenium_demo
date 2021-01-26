from configparser import ConfigParser, NoSectionError
from log.log import Log
import os


def readini(title, name):
    log = Log()
    path = os.path.dirname(os.path.dirname(__file__)) + '/config.ini'
    cf = ConfigParser()
    try:
        cf.read(path, encoding='utf-8')
        return cf.get(title, name)
    except NoSectionError as e:
        log.error('ReadError: {}'.format(e))
