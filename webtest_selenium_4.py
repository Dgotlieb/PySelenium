from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("/Users/danielgotlieb/Downloads/chromedriver"))
