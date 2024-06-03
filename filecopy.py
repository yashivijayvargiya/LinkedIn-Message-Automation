from selenium import webdriver
from time import sleep	#to use sleep function
from webdriver_manager.chrome import ChromeDriverManager
import parameters	#parameter file contains credentials
from openpyxl import load_workbook	#to use excel file
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())	#to download chromedriver
sleep(3)

#driver = webdriver.Chrome(executable_path = r'C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe')
#sleep(0.5)

driver.maximize_window()	#to maximize the tab
sleep(0.5)

driver.get('https://www.linkedin.com/')	#open this url
sleep(2)

sign_in_button = driver.find_element_by_xpath("//a[@class='nav__button-secondary btn-md btn-secondary-emphasis']")
sign_in_button.click()

# driver.find_element(By.LINK_TEXT, "Sign in")
# driver.find_element_by_xpath('//a[text()="Sign in"]').click()	#click on sign-in button
# sleep(2)

username_input = driver.find_element_by_name('session_key')	#to select textarea of username
username_input.send_keys(parameters.username) #fetch username from parameter file
sleep(0.5)

password_input = driver.find_element_by_name('session_password')	#to select textarea of username
password_input.send_keys(parameters.password)	#fetch username from parameter file
sleep(0.5)

# driver.find_element_by_xpath('//button[text()="Sign in"]').click()	#click on sign-in button
# sleep(2)
sign_in_button = driver.find_element_by_class_name("login__form_action_container")
sign_in_button.click()

book = load_workbook('C:/Users/Yashi/Downloads/LinkedIn python project/test.xlsx')#Excel File Path
Sheet = book['Sheet1']	#to select sheet


#for loop

for rows in Sheet.rows:

	arr=rows[2].value
	sleep(2)

	if str(arr)=="URL":
		continue

	driver.get(arr)
	sleep(2)	

	driver.find_element_by_link_text("Message").click()
	sleep(2)
	
	text=driver.find_element_by_xpath('//div[@aria-label="Write a message…"]/p')
	sleep(2)
    
	arr1=rows[0].value
	sleep(1)

	text.send_keys("Hey " + arr1+" " + parameters.message)
	sleep(3)

	driver.find_element_by_xpath('//button[@class="msg-form__send-button artdeco-button artdeco-button--1"]').click()#to click on close button
	sleep(2)

	driver.find_element_by_xpath('//button[@class="msg-overlay-bubble-header__control artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view"]').click()
	
print("Automation Successful")
sleep(2)
driver.quit()


