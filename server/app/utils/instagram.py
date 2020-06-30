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
import base64
import os
import string

class Instagram(WebDriver):
    def __init__(self, data, mobile=False):
        super().__init__(data, mobile)

    def redirect_to_login_page(self):
        self.browser.get("https://www.instagram.com/accounts/login/")

    def redirect_to_user_page(self, username):
        self.browser.get("https://www.instagram.com/{}/".format(username))

    def redirect_to_user_following(self, username):
        self.browser.get("https://www.instagram.com/{}/following/".format(username))

    def redirect_to(self, url):
        self.browser.get(url)

    def login(self, username, password):
        self.browser.get("https://www.instagram.com/accounts/login/")

        input = self.browserWait.until(
            presence_of_all_elements_located((By.CLASS_NAME, "_2hvTZ")))

        usernameInput = input[0]
        passwordInput = input[1]

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.ENTER)

        time.sleep(5)

    def logout(self):
        print("=========== Logout Phase ===========")
        try:
            self.browserWait.until(
                presence_of_all_elements_located((By.CLASS_NAME, "Fifk5")))[4].click()
        except Exception as identifier:
            self.browserWait.until(
                presence_of_all_elements_located((By.CLASS_NAME, "Fifk5")))[3].click()

        time.sleep(3)

        try:
            self.browserWait.until(
                presence_of_all_elements_located((By.CLASS_NAME, "aOOlW")))[7].click()
        except Exception as identifier:
            self.browserWait.until(
                presence_of_all_elements_located((By.CLASS_NAME, "_8-yf5")))[0].click()

            time.sleep(3)

            self.browserWait.until(
                presence_of_all_elements_located((By.CLASS_NAME, "aOOlW")))[8].click()

            try:
                self.browserWait.until(
                    presence_of_all_elements_located((By.CLASS_NAME, "aOOlW")))[0].click()
            except Exception as identifier:
                pass

    def like_post(self, username):
        print("Running like post using {}".format(username))
        try:
            try:
                follow_button = self.browserWait.until(
                    presence_of_all_elements_located((By.CLASS_NAME, "oW_lN")))[0]

                if follow_button.text == "Follow":
                    follow_button.click()
            except Exception as identifier:
                pass

            like = self.browserWait.until(
                presence_of_all_elements_located((By.XPATH, "//*[@class='_8-yf5 ' and @height='24' and @width='24']")))[0]

            if like.get_attribute("aria-label") == "Like":
                like.click()
                message = "{} success like post".format(username)
                self.push_notice("success", message)

                self.create_history(message)
                print(message)
            else:
                message = "{} already like post".format(username)
                self.push_notice("info", message)

                self.create_history(message)
                print(message)
        except Exception as identifier:
            print(traceback.format_exc())
            message = "{} failed like post because {}".format(username, str(identifier))
            self.push_notice("error", message)

            self.create_history(message)
            print(message)

    def comment_post(self, comment):
        textarea = self.browserWait.until(
            presence_of_element_located((By.XPATH, '//form/textarea')))
        textarea.send_keys(comment)
        textarea.send_keys(Keys.ENTER)

    def like_comment_post(self):
        self.randomCode = self.data["random_code"]

        count = models.Bot.objects.count()

        random_object = models.Bot.objects.order_by("?").all()

        total_comment = 0
        total_like = 0

        for bot in random_object:
            try:
                self.login(bot.username, bot.password)
                time.sleep(3)
                self.redirect_to(self.data["url"])

                if self.data["total_like"] > 0:
                    if total_like <= self.data["total_like"]:
                        print("break")
                        break

                time.sleep(3)
                # self.comment_post("Keren mas mantul")
                self.like_post(bot.username)

                time.sleep(3)
                self.logout()
                time.sleep(5)
            except Exception as identifier:
                print(identifier)
                pass

        self.browser.close()

    def unfollow(self):
        self.login(self.data["username"], self.data["password"])

        time.sleep(3)

        self.redirect_to_user_following(self.data["username"])

        following_link = self.browser.find_elements_by_class_name('-nal3')[-1]
        following_link.click()
        time.sleep(2)
        following_list = self.browser.find_element_by_css_selector(
            'div[role=\'dialog\'] ul')

        total_unfollow = 0

        following_list.click()
        actionChain = webdriver.ActionChains(self.browser)
        
        while total_unfollow <= self.data["total_unfollow"]:
            for follow in following_list.find_elements_by_xpath("//*[contains(text(), 'Following')]"):
                if total_unfollow <= self.data["total_unfollow"]:
                    try:
                        follow.click()

                        time.sleep(2)

                        confirmationButton = self.browserWait.until(
                            presence_of_element_located((By.CLASS_NAME, '-Cab_')))

                        username = follow.find_elements_by_xpath("//*[contains(text(), 'Unfollow')]")[0].text

                        time.sleep(2)

                        confirmationButton.click()

                        total_unfollow += 1

                        message = "{} success unfollow {}".format(self.data["username"], username.split("Unfollow @")[1].split("?")[0])

                        self.push_notice("success", message)

                        self.create_history(message)
                        print(message)

                        time.sleep(random.randint(5, 20))
                    except Exception as identifier:
                        pass

            actionChain.key_down(Keys.CONTROL).click(following_list).key_up(Keys.CONTROL).perform()
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

        self.browser.close()

    def follow_from_competitor(self, username_competitor, total_follow):
        self.login(self.data["username"], self.data["password"])

        time.sleep(3)

        self.redirect_to_user_page(username_competitor)

        following_link = self.browser.find_element_by_css_selector('ul li a')
        following_link.click()
        time.sleep(2)
        following_list = self.browser.find_element_by_css_selector(
            'div[role=\'dialog\'] ul')

        total_follow = 0

        following_list.click()
        actionChain = webdriver.ActionChains(self.browser)
        
        while total_follow <= self.data["total_follow"]:
            for follow in following_list.find_elements_by_xpath("//*[contains(text(), 'Follow')]"):
                try:
                    time.sleep(2)

                    if follow.text == "Follow" and total_follow <= self.data["total_follow"]:
                        # username = follow.find_element_by_xpath("..").find_element_by_xpath("..").find_element_by_xpath(".//*[@class='FPmhX ']").text
                        # print(username)

                        follow.click()

                        time.sleep(2)

                        total_follow += 1

                        message = "success follow"

                        self.push_notice("success", message)

                        self.create_history(message)
                        print(message)

                        time.sleep(random.randint(5, 20))
                except Exception as identifier:
                    print(identifier)
                    pass

            actionChain.key_down(Keys.CONTROL).click(following_list).key_up(Keys.CONTROL).perform()
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

        self.browser.close()

    def randomString(self, stringLength=8):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def multiple_post(self, title, description, image, accounts):
        image_path = os.getcwd() + "/assets/images/" + self.randomString(20) + ".png"
        
        with open(image_path, "wb") as fh:
            fh.write(base64.b64decode(image.split("data:image/png;base64")[1]))

        for account in accounts:
            self.login(account["username"], account["password"])
            self.redirect_to("https://instagram.com")

            time.sleep(3)

            try:
                self.browserWait.until(
                presence_of_element_located((By.XPATH, "//*[contains(text(), 'Cancel')]"))).click()
            except Exception as identifier:
                pass

            time.sleep(4)

            try:
                self.browserWait.until(presence_of_element_located((By.XPATH, "//*[contains(text(), 'Not Now')]"))).click()
            except Exception as identifier:
                pass

            # self.browser.find_elements_by_xpath('//*[@aria-label="New Post"]')[0].click()
            # self.browser.switch_to.active_element.send_keys(image_path)
            self.browser.find_elements_by_xpath('//*[@class="tb_sK"]')[3].send_keys(image_path)
            self.browser.find_elements_by_xpath('//*[@class="Q9en_"]')[0].submit()

            time.sleep(2)
            self.browser.find_elements_by_xpath('//*[contains(text(), "Next")]')[0].click()
            self.browser.find_elements_by_xpath('//*[@aria-label="Write a caption…"]')[0].send_keys(description)
            time.sleep(2)
            self.browser.find_elements_by_xpath('//*[contains(text(), "Share")]')[0].click()


    def follow_from_post(self, url):
        # Login instagram
        self.login(self.data["username"], self.data["password"])

        time.sleep(3)

        # Redirect ke postingan
        self.redirect_to(url)

        time.sleep(3)

        # Klik daftar menyukai
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[2]/div/div/button').click()

        time.sleep(3)

        # Ambil data pengguna yang menyukai
        following_list = self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div')

        following_list.click()
        actionChain = webdriver.ActionChains(self.browser)

        next = True
        
        while next:
            follows = following_list.find_elements_by_xpath("//*[contains(text(), 'Follow')]")

            for follow in follows:
                try:
                    time.sleep(2)

                    if follow.text == "Follow":
                        try:
                            username = follow.find_element_by_xpath("..").find_element_by_xpath("..").find_element_by_xpath(".//*[@class='FPmhX ']").text
                        except Exception as identifier:
                            username = ""

                        follow.click()

                        time.sleep(2)

                        message = "success follow {}".format(username)

                        self.push_notice("success", message)

                        self.create_history(message)
                        print(message)

                        time.sleep(random.randint(5, 20))
                except Exception as identifier:
                    print(identifier)
                    pass

            actionChain.key_down(Keys.CONTROL).click(following_list).key_up(Keys.CONTROL).perform()
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

            if len(follows) == 0:
                next = False

        self.browser.close()