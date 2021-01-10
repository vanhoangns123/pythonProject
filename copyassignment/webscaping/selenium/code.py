from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Driver specification and executable path
driver = webdriver.Chrome(executable_path="C://Users//vinhn//OneDrive//Documents//pythonProject//copyassignment//webscaping//chromedriver.exe")
# Redirects to the specified website
driver.get("https://copyassignment.com/")
#specifies the input element in the website
search_element = driver.find_element_by_id("is-search-input-0")

text = "Turtle" # sends the keys to the input field
search_element.send_keys("Turtle")