from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located, presence_of_all_elements_located
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path
from datetime import datetime
from random import randint
import platform
import traceback
import time
import os
import pusher

from app import models


class WebDriver():
    def __init__(self, data):
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--start-maximized")
        chromeOptions.add_experimental_option(
            "prefs", {"intl.accept_languages": "en,en_US"})

        self.browser = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(), options=chromeOptions)
        self.browserWait = WebDriverWait(self.browser, 10)

        self.pusher = pusher.Pusher(app_id="1023722", key="81ac97583b4547cbf23a", secret="dc7dbf82834517f09ebd", ssl=True, cluster="ap1")
        self.randomCode = ""
        self.data = data

    def create_history(self, description):
        return models.History.objects.create(description=description, created_date=datetime.now())

    def push_notice(self, type, message):
        self.pusher.trigger("notice", "log-{}".format(self.data["random_code"]), {
            "type": type,
            "message": message
        })

        return self.pusher.trigger("notice", "log", {
            "type": type,
            "message": message
        })