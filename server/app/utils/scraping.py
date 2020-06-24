from selenium.webdriver.support.expected_conditions import presence_of_element_located, presence_of_all_elements_located
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

from .webdriver import WebDriver

from datetime import datetime
from app import models
import traceback
import time
import random

class Scraping(WebDriver):
    def __init__(self, data):
        super().__init__(data)

    def scrape_data(self, keyword):
        tag, created = models.Tag.objects.get_or_create(name=keyword)

        self.browser.get("https://www.google.com/maps/search/{}".format(keyword))

        while True:
            try:
                time.sleep(2)
                index = 0
                rows = self.browserWait.until(presence_of_all_elements_located(
                    (By.XPATH, '//*[@class="section-result"]')))

                for i in range(len(rows)):
                    try:
                        rows = self.browserWait.until(presence_of_all_elements_located(
                            (By.XPATH, '//*[@class="section-result"]')))

                        for idx, row in enumerate(rows):
                            if idx != index:
                                continue

                            row.click()
                            title = ""
                            phone = ""
                            address = ""
                            website = ""

                            try:
                                xpath = '//*[@class="section-hero-header-title"]/div[@class="section-hero-header-title-description"]/div[1]/h1'

                                title = self.browserWait.until(
                                    presence_of_element_located((By.XPATH, xpath))).text
                            except Exception as identifier:
                                print(identifier)

                            try:
                                xpath = '//button[@data-tooltip="Salin alamat"]/div[1]/div[2]/div[1]'
                                address = self.browserWait.until(presence_of_element_located(
                                    (By.XPATH, xpath))).text
                            except Exception as identifier:
                                pass

                            try:
                                xpath = '//button[@data-tooltip="Buka situs"]/div[1]/div[2]/div[1]'
                                website = self.browserWait.until(presence_of_element_located(
                                    (By.XPATH, xpath))).text
                            except Exception as identifier:
                                pass

                            try:
                                xpath = '//button[@data-tooltip="Salin nomor telepon"]/div[1]/div[2]/div[1]'
                                phone = self.browserWait.until(presence_of_element_located(
                                    (By.XPATH, xpath))).text
                            except Exception as identifier:
                                pass

                            contact, created = models.Contact.objects.get_or_create(
                                name=title,
                                website=website,
                                address=address,
                                phone=phone,
                            )

                            if created:
                                contact.tags.add(tag)

                                message = "contact with name {} has been saved".format(title)
                                self.push_notice("success", message)
                                self.create_history(message)

                            index += 1

                            self.browserWait.until(presence_of_element_located(
                                (By.CLASS_NAME, "section-back-to-list-button"))).click()

                            time.sleep(2)
                    except Exception as identifier:
                        # print (identifier)
                        pass

                self.browserWait.until(presence_of_element_located(
                    (By.XPATH, '//*[@aria-label="Halaman berikutnya"]'))).click()
            except Exception as identifier:
                print(identifier)
                break

        self.browser.close()