#!/usr/bin/env python
# coding=utf-8
import os, time, random
from selenium import webdriver
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

with open("names", encoding='utf-8') as f:
    content = f.readlines()
content = [x.strip() for x in content]
driver = webdriver.Firefox(executable_path=os.path.abspath("../geckodriver.exe"))
url = "https://goo.gl/forms/3kRPM1phQrSSL0Mx1"

# Login
try:
    lst = list(range(len(content)))
    random.shuffle(lst)
    for i in lst:
        driver.get(url)
        myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='freebirdFormviewerViewHeaderTitle']")))
        email = "s15" + str(randint(1000, 9999)) + "@student.dhbw-mannheim.de"
        driver.find_element_by_xpath("//input[@name='emailAddress']").send_keys(email)
        driver.find_element_by_xpath("//input[@aria-label='Name:']").send_keys(content[i])
        time.sleep(2)
        driver.find_element_by_xpath("//span[@class='quantumWizButtonPaperbuttonLabel exportLabel']").click()
except TimeoutException:
    print("hi")
