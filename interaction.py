from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, value='fName')
first_name.send_keys("merab")
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("todua")
email_address = driver.find_element(By.NAME, value="email")
email_address.send_keys("dasdasasasdasdw@gmail.com")
button = driver.find_element(By.TAG_NAME, "button")
button.click()



# driver.quit()



