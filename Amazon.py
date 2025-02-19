from selenium.webdriver import keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


# automate the TC: Simple google search
print("#step 1 open google chrome browser")
url='https://www.google.com/'
driver=webdriver.Chrome()
#time.sleep()






# amazon case, will not work unless u open website
driver.get("www.amazon.com")
products=driver.find_elements(By.ID, 'gridItemRoot') #returns u python list
products[0].click()
driver.back()
products[-1].click()  #cliking on the last product
