from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

users = ['user@gmail.com']
passws =  ['azazada']


@pytest.mark.parametrize('creds', [('user@gmail.com', 'azazada')])
def test_login(creds):
    login, passw = creds
    driver = webdriver.Chrome()
    driver.get('https://magento.softwaretestingboard.com/customer/account/login')
    driver.find_element(By.ID, 'email').send_keys(login)
    driver.find_element(By.ID, 'pass').send_keys(passw)
    driver.find_element(By.ID, 'send2').click()

    error_text = driver.find_element(By.CSS_SELECTOR, '[data-ui-id="message-error"]').text
    assert (
            'The account sign-in was incorrect or your account is disabled temporarily. '
            'Please wait and try again later.'
            == error_text
    )


# @pytest.fixture()
# def page(request):
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(5)
#     driver.get('https://magento.softwaretestingboard.com/sale.htm')
#     return driver


@pytest.fixture()
def page(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    param = request.param
    if param == 'wats_new':
        driver.get('https://magento.softwaretestingboard.com/what-is-new.html')
    elif param == 'sale':
        driver.get('https://magento.softwaretestingboard.com/sale.html')
    return driver


@pytest.mark.parametrize('page', ['wats_new'], indirect=True)
def test_whats_new(page):
    title = page.find_element(By.CSS_SELECTOR, 'h1')
    assert title.text == 'What\'s New'


@pytest.mark.parametrize('page', ['sale'], indirect=True)
def test_sale(page):
    title = page.find_element(By.CSS_SELECTOR, 'h1')
    assert title.text == 'Sale'
