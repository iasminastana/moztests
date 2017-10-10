from ..pages.login import Login

_USERNAME = 'admin'
_PASSWORD = 'asdf'
_URL = 'http://172.16.228.215:8080/'


def test_login(selenium):
    login_page = Login(selenium, _URL)
    dashboard = login_page.login(_USERNAME, _PASSWORD)
    assert dashboard.expected_title == dashboard.get_page_title()
