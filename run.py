import pytest
import os

reportpath = os.getcwd()+'//report.html'


def run():
    pytest.main(["-s", '-v', "--html=report.html"])


if __name__ == '__main__':

    print("开始main")
    if os.path.isfile(reportpath):
          os.remove(reportpath)
          run()
    else:
        run()
