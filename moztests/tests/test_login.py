from ..pages.homepage import HomePage


def test_login(selenium, variables):
    login_page = HomePage(selenium, variables)
    dashboard = login_page.login(variables['username'], variables['password'])
    assert dashboard.expected_title == dashboard.get_page_title()
