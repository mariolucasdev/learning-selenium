from constants import host, user, pswd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

driver.get(host)
driver.implicitly_wait(0.5)

input_login = driver.find_element(By.ID, "username")
input_password = driver.find_element(By.ID, "password")

input_login.send_keys(user)
input_password.send_keys(pswd,  Keys.ENTER)

driver.quit()