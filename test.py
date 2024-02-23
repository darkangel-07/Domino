from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

def use_proxy(proxy):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % proxy)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://checkip.amazonaws.com")


    body_text = driver.find_element(By.TAG_NAME, "body").text
    print(f"Proxy: {proxy}, IP: {body_text}")

    # If the proxy is working, visit https://www.car-part.com/
    if body_text.strip() == proxy.split(':')[0]:
        print(f"Proxy {proxy} is working. Now visiting https://www.car-part.com/")
        driver.get("https://www.car-part.com/")
        time.sleep(3)
        # Add your code here to interact with the website

    

# Scrape the proxies
url = "https://www.us-proxy.org/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

proxy_array = []
for row in soup.find('table').find_all('tr'):
    columns = row.find_all('td')
    if columns:
        ip = columns[0].get_text()
        port = columns[1].get_text()
        proxy_array.append(f"{ip}:{port}")

# Use the proxies with Selenium
for proxy in proxy_array:
    use_proxy(proxy)