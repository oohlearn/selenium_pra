from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

# scrape website
response = requests.get("https://appbrewery.github.io/Zillow-Clone/").text
soup = BeautifulSoup(response, "html.parser")
link_list = soup.find_all("a", class_="property-card-link")
links = [link.get("href") for link in link_list]

price_list = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
prices = [price.text for price in price_list]
prices_clean = [price.replace("/mo", "").split("+")[0] for price in prices]
print(prices_clean)

address_list = soup.select("a address")
addresses = [address.text for address in address_list]
address_clean =[]
for address in addresses:
    address = address.replace("\n", "")
    address = address.replace("|", "")
    address = address.replace("  ", "")
    address_clean.append(address)

# scrape google sheet
chrome_options = webdriver.ChromeOptions()  
chrome_options.add_experimental_option("detach", True)

# 初始化WebDriver
driver = webdriver.Chrome(options=chrome_options)

# 打開網頁

# address price link
for i in range(len(address_clean)):
    driver.get('https://forms.gle/h6aXuPgoD9xAzK2x9')

    time.sleep(2)
    
    submit_btn = driver.find_element(By.CSS_SELECTOR, ".Y5sE8d span span")

    form_address = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_price = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_link = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    
    form_address.send_keys(address_clean[i])
    form_price.send_keys(prices_clean[i])
    form_link.send_keys(links[i])
    submit_btn.click()

driver.quit()

