from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper.xpath import xpath as x


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_homepage(self):
        button = self.driver.find_element(By.XPATH, x.logo)
        button.click()

    def open_about(self):
        button = self.driver.find_element(By.XPATH, x.abount_button)
        button.click()

    def open_delivery_and_payment(self):
        button = self.driver.find_element(By.XPATH, x.delivery_and_payment)
        button.click()

    def open_refund_replacement(self):
        button = self.driver.find_element(By.XPATH, x.refund_replacement)
        button.click()

    def open_contacts(self):
        button = self.driver.find_element(By.XPATH, x.contacts)
        button.click()

    def open_helps(self):
        button = self.driver.find_element(By.XPATH, x.helps)
        button.click()

    def open_feedbacks(self):
        button = self.driver.find_element(By.XPATH, x.feedbacks)
        button.click()

    def open_dropshipping(self):
        button = self.driver.find_element(By.XPATH, x.dropshipping)
        button.click()

    def open_categories(self):
        button = self.driver.find_element(By.XPATH, x.categories)
        button.click()

    def open_categories_new_products(self):
        button = self.driver.find_element(By.XPATH, x.new_products)
        button.click()

    def open_categories_tactical_clothing(self):
        button = self.driver.find_element(By.XPATH, x.tactical_clothing)
        button.click()

    def open_categories_tactical_shoes(self):
        button = self.driver.find_element(By.XPATH, x.tactical_shoes)
        button.click()

    def open_categories_tourism_camping(self):
        button = self.driver.find_element(By.XPATH, x.tourism_camping)
        button.click()

    def open_categories_military_equipment(self):
        button = self.driver.find_element(By.XPATH, x.military_equipment)
        button.click()

    def open_categories_tactical_equipment(self):
        button = self.driver.find_element(By.XPATH, x.tactical_equipment)
        button.click()

    def open_categories_components(self):
        button = self.driver.find_element(By.XPATH, x.components)
        button.click()

    def open_categories_optics(self):
        button = self.driver.find_element(By.XPATH, x.optics)
        button.click()

    def open_categories_backpacks(self):
        button = self.driver.find_element(By.XPATH, x.backpacks)
        button.click()

    def open_categories_fishing_and_hunting(self):
        button = self.driver.find_element(By.XPATH, x.fishing_and_hunting)
        button.click()

    def open_categories_trainers(self):
        button = self.driver.find_element(By.XPATH, x.trainers)
        button.click()
