
![Screenshot](screeshot.png)

# Twitter AutoPoster Bot 
 
## Table of contents
* [Description](#description)
* [Depedencies](#depedencies)
* [Setup](#setup)
* [Features](#features)
* [License](#license)

## Description
This is a Command-Line Interface for a Twitter Bot written in Python.
	
## Dependencies
Project is created with:
* Python version: 3.6.8
* Tweepy version: 3.8.0
* Selenium library version: 3.141.0
	
## Setup
To run this project, download the `twitbot.py` Python Script after cloning this repository.
Python 3.6 or higher is preferred for smooth running, also Tweepy and Selenium must be installed.

#### Installing Python 3.6 
Try [this](https://askubuntu.com/questions/865554/how-do-i-install-python-3-6-using-apt-get).

#### Installing Tweepy
Try [this](https://stackoverflow.com/questions/31325305/install-tweepy-on-ubuntu).

#### Installing Selenium
This Script has been written for the Firefox browser.  
Try [this](https://askubuntu.com/questions/937770/how-to-install-and-set-up-selenium-webdriver-on-ubuntu-16-04) to install Selenium, and [this](https://askubuntu.com/questions/851401/where-to-find-geckodriver-needed-by-selenium-python-package) for geckodriver required for Firefox(likewise ChromeDriver for Chrome).

Now execute this script from the terminal using `python twitbot.py`.  
You will be prompted for your username and password, once they are specified, this script automatially logs in to your Twitter Account.

## Features
* Automatic Login(prompts user for username and password on the terminal)
* Retweets based on specified keyword
* Likes Tweets based on specified keyword
* Posts insightful links(reads insightful links from a file and posts them as tweets)
* Replies to Tweets having a specified keyword

## License
The LICENSE can be found [here](LICENSE).

