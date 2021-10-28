from selenium import webdriver
path = "/home/dhanya/Downloads/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://en.wikipedia.org/wiki/Data")
data = driver.find_element_by_tag_name('p')
print(data)
