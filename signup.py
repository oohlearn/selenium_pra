from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()  
chrome_options.add_experimental_option("detach", True)

# 初始化WebDriver
driver = webdriver.Chrome(options=chrome_options)

# 打開網頁
driver.get('https://secure-retreat-92358.herokuapp.com/')

# first name
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("123")

# last name
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("456")

# email address
email_address = driver.find_element(By.NAME, "email")
email_address.send_keys("test@123")

# click sign up btn
signup_btn = driver.find_element(By.XPATH, "/html/body/form/button")
signup_btn.click()

# 用按鍵
# search = driver.find_element(By.NAME, "search")
# search.send_keys("python", Keys.ENTER)

