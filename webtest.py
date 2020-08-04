from selenium import webdriver

# Windows:
driver = webdriver.Chrome(executable_path="C:\\Users\user\Desktop\ChromeDriver.exe")

# Mac and linux:
driver = webdriver.Chrome(executable_path="/users/user/chromedriver")
