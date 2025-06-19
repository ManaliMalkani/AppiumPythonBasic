import pytest

#pytest --reruns 5 testRerun.py
@pytest.mark.flaky(reruns=5)
def test_methodOne():
    var1 = 1
    var2 = 2
    assert var1 == var2