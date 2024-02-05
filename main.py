from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/") 
big_cookie = driver.find_element(By.ID, value="cookie")
money = driver.find_element(By.ID, value="money")
store = driver.find_element(By.ID, value="store")
div_in_store = store.find_elements(By.TAG_NAME, value="div")
count =0


while True:
    count += 1
    big_cookie.click()
    pr_list = []
    

    if "," in money.text:
        clean_money = money.text.replace(",", "")
        int_money = int(clean_money)
    else:
        int_money = int(money.text)



    for x in div_in_store:
        prices = x.find_element(By.TAG_NAME, value="b").text
        if len(prices.split(" - ")) > 1:
            if "," in prices.split(" - ")[1]:
                clean_price = prices.split(" - ")[1].replace(",", "")
                grayed = x.get_attribute("class") != "grayed" 
                if grayed:
                    pr_list.append(int(clean_price))
            else:
                grayed = x.get_attribute("class") != "grayed"
                if grayed:
                    pr_list.append(int(prices.split(" - ")[1]))
        else:
            break 

    # def buy():             
    #     for y in pr_list:
    #       if int_money >= y and y == max(pr_list):
    #           selected_item = div_in_store[pr_list.index(y)]
    #           selected_item.click()
    #     return time.sleep(6)            
    # if count >= 15 :
    #     big_cookie.click()
    #     buy()
           
                
driver.quit()
