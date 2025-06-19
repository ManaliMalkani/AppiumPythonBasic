import pytest


print("This is a Run Order class")

@pytest.mark.order(4)
def test_methodA():
    print("This is method A")

@pytest.mark.order(3)
def test_methodB():
    print("This is method B")

@pytest.mark.order(1)
def test_methodC():
    print("This is method C")

@pytest.mark.order(2)
def test_methodD():
    print("This is method D")