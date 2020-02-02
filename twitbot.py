import tweepy
import time
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


FILE_NAME = 'last_seen_id.txt'


class TwitterBot:

	def __init__(self,CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET):
	
		print('Twitter Bot on Work Mode! :P')
		self.CONSUMER_KEY = CONSUMER_KEY
		self.CONSUMER_SECRET = CONSUMER_SECRET
		self.ACCESS_KEY = ACCESS_KEY
		self.ACCESS_SECRET = ACCESS_SECRET
		self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		self.auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
		self.api = tweepy.API(self.auth) #this object is used to read data into twitter and write data to it.

		

	def retrieve_last_seen_id(self,file_name):
		f_read = open(file_name, 'r')
		last_seen_id = f_read.read().strip()
		f_read.close()
		return last_seen_id #id of the last tweet we replied to.
	
	
	def store_last_seen_id(self, last_seen_id, file_name):
		f_write = open(file_name, 'w')
		f_write.write(str(last_seen_id))
		f_write.close()
		return
	
	
	
	def post_links(self):
		print('posting linsk')
		x=0
		file1 = open('newfile.txt','r')
		line = file1.readline().strip()
		while(line != ''):
			print('line '+str(x)+' '+line)
			print(line+'\n')
			line = file1.readline().strip()
			self.api.update_status(status = str(line + '\n(Posted by dvlpshbot. If you like this content, please share your feedback.)'))
			x=x+1
		file1.close()
		print('Updated links')
	
	
	
	def retweets(self, search_string,number_of_tweets):
		for tweet in tweepy.Cursor(self.api.search, search_string).items(number_of_tweets):
			try:
				tweet.retweet()
				print("Retweeting")
			except tweepy.TweepError as e:
				print(e.reason)
			except StopIteration:
				break
	
	def favorite(self,search_string,number_of_tweets):
		for tweet in tweepy.Cursor(self.api.search, search_string).items(number_of_tweets):
			try:
				tweet.favorite()
				print("Tweet Liked")
			except tweepy.TweepError as e:
				print(e.reason)
			except StopIteration:
				break


	def reply_to_tweets(self, search_string):
		last_seen_id = retrieve_last_seen_id(FILE_NAME)
		mentions = self.api.mentions_timeline(tweet_mode = 'extended') #mention is like a list so we can iterate through it

		x=1
		for mention in reversed (mentions): #go through tweets in chronological order
			print(str(mention.id)+ ' --> '+ mention.full_text)
			if (search_string in mention.full_text.lower()):
				print('Found!\n')
				print('Replying back in a jiffy!')
				self.api.update_status(status = str('Responding to tweet '+str(x)+' @'+mention.user.screen_name+' :P'), in_reply_to_status_id = mention.id, auto_populate_reply_metadata=True)
				x=x+1
			else :	
				print('NOT FOUND!!!\n')
		


	def login(self, username, password):
		driver = webdriver.Firefox()
		driver.get("https://twitter.com/")
		print("Visiting ", driver.title)
		driver.implicitly_wait(5)
	
		driver.find_element_by_link_text("Log in").click();
		email_xpath1 = '/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input'
		email_xpath2 = '/html/body/div/div/div/div/main/div/div/form/div/div[1]/label/div[2]/div/input'
	
		password_xpath1 = '/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input'
		password_xpath2 = '/html/body/div/div/div/div/main/div/div/form/div/div[2]/label/div[2]/div/input'
	
		time.sleep(2)
	
		try:
			email_element = driver.find_element_by_xpath(email_xpath2)
			password_element = driver.find_element_by_xpath(password_xpath2)
			
		except NoSuchElementException:
			email_element = driver.find_element_by_xpath(email_xpath1)
			password_element = driver.find_element_by_xpath(password_xpath1)
	
		email_element.send_keys(username)
		password_element.send_keys(password)
		time.sleep(2)
		password_element.send_keys(Keys.RETURN)
		print("Login Complete!")
			

def main():
	
	CONSUMER_KEY = getpass("CONSUMER KEY  : ")
	CONSUMER_SECRET = getpass("CONSUMER SECRET KEY  : ")
	ACCESS_KEY = getpass("ACCESS KEY  : ")
	ACCESS_SECRET = getpass("ACCESS SECRET KEY : ")
	
	twitbot = TwitterBot(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
	
	flag=0
	
	while flag!=1:
		choice=int(input('1.Log in?\n2.Post links\n3.Respond to tweets having specified keyword\n4.Retweet based on a specified keyword\n5.Like Tweets based on a specified keyword\n\nPress -1 to Exit\n\nEnter your choice:'))
		if choice == 1:
			username = input("user name : ")
			password = getpass("password  : ")
			twitbot.login(username, password)
		
		elif choice == 2:
			twitbot.post_links()
			
		elif choice == 3:
			search_string = input('Enter the keyword to search for in Tweet: ')
			twitbot.reply_to_tweets(search_string)
		
		elif choice == 4:
			search_string = input('Enter the keyword to search for in Tweet: ')
			number_of_tweets = int(input('Enter number of retweets: '))
			twitbot.retweets(search_string,number_of_tweets)
			
		elif choice == 5:
			search_string = input('Enter the keyword to search for in Tweet: ')
			number_of_tweets = int(input('Enter number of retweets: '))
			twitbot.favorite(search_string,number_of_tweets)
		
		
		elif choice == -1:
			flag=1

		else:
			print('Invalid Choice. Enter a valid number.\n')

	
if __name__ == "__main__":
	main()
#1082163594190417920-xPxtAlkuVyvcIwsaI7Mo8aNmTiKTJV
#TgNNT7HStTZklXsNNeHDUWkYrqAzISazkLZF59Kx5sIpz
