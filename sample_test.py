from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestMy:

    def setup_method(self):
        self.driver: WebDriver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.google.ru/")

    def test_01hello_world(self):
        self.driver.find_element_by_name("q").send_keys("Moscow Stock Exchange Repository\n")

    def test_02hello_world(self):
        self.driver.find_element_by_id("resultStats")
        assert WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "resultStats")).is_displayed())

    def teardown_method(self):
        self.driver.close()
