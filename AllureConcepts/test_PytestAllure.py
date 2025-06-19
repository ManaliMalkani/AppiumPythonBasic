#pip3 install allure-pytest
#brew install allure
#allure --version
#https://allurereport.org/docs/install-for-macos/
#pytest --alluredir=../AllureReports -v -s test_PytestAllure.py
#allure generate ../AllureReports -o ../AllureReports/html --clean
#allure open ../AllureReports/html


import pytest
import allure

@allure.title("Test Method A")
@allure.description("This test checks functionality A")
@pytest.mark.order(4)
def test_methodA():
    print("This is method A")

@allure.title("Test Method B")
@allure.description("This test checks functionality B")
@pytest.mark.order(3)
def test_methodB():
    print("This is method B")

@pytest.mark.order(1)
#@pytest.mark.skip
def test_methodC():
    print("This is method C")

@pytest.mark.order(2)
def test_methodD():
    print("This is method D")