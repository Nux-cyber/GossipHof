# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
time.sleep(5)
username = driver.find_element_by_name('username')
username.send_keys("NotAnonymus123", Keys.ARROW_DOWN)
password = driver.find_element_by_name('password')
password.send_keys("Passwort")
time.sleep(1.2)
password.submit()
time.sleep(15)
gossip = driver.find_element_by_name("Suchen")
gossip.send_keys("hof.gossip.000")