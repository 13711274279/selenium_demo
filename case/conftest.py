import pytest


@pytest.fixture(scope="session")
def init_session():
    print("回话前置")
    yield
    print("回话后置")


@pytest.fixture(scope="module")
def init_module():
    print("模块前置")
    yield
    print("模块后置")


@pytest.fixture(scope="class")
def init_class():
    print("类的前置")
    yield
    print("类的后置")


@pytest.fixture(scope="function")
def init_function():
    print("用例前置")
    a = "111"
    b = "222"
    yield a, b
    print("用例后置")

