import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_submit_button_visibility(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[value="Добавить в корзину"]'))
    )
    time.sleep(10)
    assert button.is_displayed() == True, "The button doesn't display"
