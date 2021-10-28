from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd

path = "/home/elakia/softwares/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(path)


driver.get("https://en.wikipedia.org/wiki/Data_science")


que = driver.find_element_by_id("bodyContent").text

# que.send_keys("chicken biryani")
print(que)


time.sleep(3)

# que.send_keys(Keys.ARROW_DOWN)

# que.send_keys(Keys.RETURN)
def reading_csv():
   
    df = pd.read_csv("wiki.csv")
    urls=df['kaggle_links']
    for url in urls:
        kaggle_details(url)