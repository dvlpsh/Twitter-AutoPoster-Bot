from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait

def login_twit(usnm, pw):
	driver = webdriver.Firefox()
	driver.get("https://twitter.com/")
	#print("Visiting ", driver.title)
	driver.find_element_by_link_text("Log in").click();
	username = driver.find_element_by_class_name("js-username-field")
	passw = driver.find_element_by_class_name("js-password-field")
	username.send_keys(usnm)
	driver.implicitly_wait(1)
	passw.send_keys(pw)
	driver.implicitly_wait(2)
	driver.find_element_by_class_name("EdgeButtom--medium").click()
	text_box = driver.find_element_by_id('tweet-box-home-timeline') #sending description
	text_box.send_keys("hello!")

if __name__ == "__main__":
    username = input("user name : ")
    password = getpass("password  : ")
    login_twit(username, password)


