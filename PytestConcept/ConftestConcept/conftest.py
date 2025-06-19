# https://pypi.org/project/pytest-rerunfailures/
# Install the package
#
# To uninstall the package type : pip uninstall pakckage_name
#
# To check whether package is installed or nor type : pip list
#
# Add the pytest marker on top of the test method.

import pytest


@pytest.fixture(scope='module')
def beforeClass():
    print('Before Class')
    yield
    print('After Class')

@pytest.fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')