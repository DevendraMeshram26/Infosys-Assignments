from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "https://www.imdb.com"
driver.get(url)
search_box = driver.find_element(By.ID,"suggestion-search")
search_box.send_keys("The Shawshank Redemption")
search_box.send_keys(Keys.RETURN)
 
time.sleep(1)

first_result = driver.find_element(By.CSS_SELECTOR, "#__next > main > div.ipc-page-content-container.ipc-page-content-container--full.sc-f91e97af-0.jbRgdG > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid__item.ipc-page-grid__item--span-2 > section:nth-child(4) > div.sc-b03627f1-2.gWHDBT > ul > li:nth-child(1) > div.ipc-metadata-list-summary-item__c > div > a")
first_result.click()
time.sleep(1)

title = driver.find_element(By.CLASS_NAME , "hero__primary-text").text
rating = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/span/div/div[2]/div[1]/span[1]").text
year = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/ul/li[1]/a" ).text
duration =driver.find_element(By.XPATH, "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/ul/li[3]").text

print("Title = " , title)
print("Rating = " , rating)
print("Year = " , year)
print("Duration = ", duration)

driver.quit()