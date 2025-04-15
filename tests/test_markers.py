import pytest

@pytest.mark.smoke
def test_some_case():
    ...

@pytest.mark.regression
def test_regression_case():
    ...

@pytest.mark.ui
class TestSuite:
    def test_case1(self):

        ...

    def test_cases2(self):

        ...


@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_case1(self):
        ...

    @pytest.mark.slow
    def test_cases2(self):
        ...
