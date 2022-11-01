from selenium.webdriver.common.by import By


class TestPlan:
    def test_multilanguage(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)

        button_find = browser.find_element(By.XPATH, "//button[@class= 'btn btn-lg btn-primary btn-add-to-basket']")
        assert button_find, 'Кнопка не найдена'
