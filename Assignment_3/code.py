# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(5)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("Book shelf")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)


# Selecting a picture 
Book_shelf_link = driver.find_element("xpath","//html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[1]/div/div/div[1]/div[2]/div[1]/div/div[1]/a/div")
#Book_shelf_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
Book_shelf_link.click()
time.sleep(4)



# Selecting a link 
Living_room_link = driver.find_element("xpath","/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[7]/div/a/span/span")
#Living_room_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
Living_room_link.click()
time.sleep(4)




# Selecting a link 
movies_link = driver.find_element("xpath","/html/body/div[1]/header/div/div[4]/div[3]/div/div/a/img")
#movies_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
movies_link.click()
time.sleep(4)


driver.close()





