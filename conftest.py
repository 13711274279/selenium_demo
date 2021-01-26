import pytest
from py._xmlgen import html


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: xx测试中心")])
    prefix.extend([html.p("测试人员: xxxxx")])


def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "测试接口项目"
    config._metadata['接口地址'] = 'http://hrmtestt.bndxqc.com'
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")
