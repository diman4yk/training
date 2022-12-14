import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options



@pytest.fixture
def get_chrom_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1650,900')
    return options

@pytest.fixture
def get_webdriver(get_chrom_options):
    options = get_chrom_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://morella-tex.ru/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies()
    yield driver
    driver.quit()