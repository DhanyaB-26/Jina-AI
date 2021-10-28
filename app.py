from selenium import webdriver
import time
import pandas as pd

def url_access(url):
        driver.get(url)
        que = driver.find_element_by_id("bodyContent").text
        time.sleep(3)
        file = open('jina.txt','a')
        file.write(que)
        file.write("\n\n\n____________________________________________________________________________________\n\n\n")
        file.write("\n\n\n____________________________________________________________________________________\n\n\n")
        file.close()
    
path = "/home/dhanya/Downloads/chromedriver"
driver = webdriver.Chrome(path)
df = pd.read_csv("wiki.csv")
urls = df['wiki_links']
for url in urls:
    url_access(url)
