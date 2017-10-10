from ..pages.login import Login


def test_login(selenium, variables):
    login_page = Login(selenium, variables)
    dashboard = login_page.login(variables['username'], variables['password'])
    assert dashboard.expected_title == dashboard.get_page_title()
