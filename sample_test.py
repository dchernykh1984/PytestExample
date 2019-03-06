from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestMy:

    def setup_method(self):
        print("Open google page")
        self.driver: WebDriver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.google.ru/")

    def test_01hello_world(self):
        print("Try to search in google")
        self.driver.find_element_by_name("q").send_keys("Moscow Stock Exchange Repository\n")
        print("Check results stats appeared")
        self.driver.find_element_by_id("resultStats")
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "resultStats")))
        assert element.is_displayed()

    def teardown_method(self):
        self.driver.close()
