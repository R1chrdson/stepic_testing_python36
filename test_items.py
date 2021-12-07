from selenium.webdriver.common.by import By

class TestLogin:
    def test_add_basket_button_present(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
        browser.get(link)
        
        button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')

        assert button, 'There is no "add to basket" button'
