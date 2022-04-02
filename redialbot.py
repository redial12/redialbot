import time
import re
from venv import create
import emoji
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Person import Person

#setting driver selenium is running off of and initializing some variables used across the methods

global file
file = open("data.txt", "w", encoding="utf-8")
global list
list = []
global linklist
linklist = []

#replaces all emojis with an empty character
def strip_emoji(text):
    new_text = emoji.replace_emoji(text, replace='')
    return new_text

#returns handle starting with an '@'
def get_handle(text):
    text_split = text.split(" ")

    for x in range(len(text_split)):
        if(text_split[x].startswith("@")):
            cutoff = text_split[x].find("\n")
            if(cutoff == -1):
                return text_split[x]
            else:
                return text_split[x][0:cutoff]
    return "NO_HANDLE"

def get_bio():
    # if the post does not have a bio, return an empty String
    notPresent = len(driver.find_elements(By.CSS_SELECTOR, "._7UhW9.xLCgt.MMzan.KV-D4.se6yk.T0kll")) < 1
    if(notPresent):
        return ""
    #otherwise get the bio, convert to lowercase, remove emojis, and return
    postbio = driver.find_element(By.CSS_SELECTOR, "._7UhW9.xLCgt.MMzan.KV-D4.se6yk.T0kll")
    posttext = postbio.text.lower()
    return strip_emoji(posttext)

# gets all posts in list and converts them to a list of links
def add_to_list():
    posts_list = driver.find_elements(By.CSS_SELECTOR, ".v1Nh3.kIKUG._bz0w [href]")
    for x in range(len(posts_list)):
        if(posts_list[x].get_attribute("href") not in linklist):
            linklist.append(posts_list[x].get_attribute("href"))

def create_data(first, second):
    for x in range(len(linklist)):

        # gets list of post links
        driver.get(linklist[x])

        time.sleep(2)
        #get post text next
        posttext = get_bio()

        #gets condition and checks for it in instagram bio
        condition = [first, second]

        CONDITION_ONE = condition[0] in posttext
        CONDITION_TWO = condition[1] in posttext

        #get handle
        handle = get_handle(posttext)

        #adds object to a list
        list.append(Person(handle, linklist[x], CONDITION_ONE, CONDITION_TWO))
        #prints object values and writes them to file
        list[x].display()
        file.write(list[x].to_string())

    
def create_data_captions():
    for x in range(len(linklist)):
    # gets list of post links
        driver.get(linklist[x])

        time.sleep(2)
        #get post text next
        posttext = get_bio()

        #prints caption text and writes them to file
        print(posttext + "\nLink: " + linklist[x] + "\n" + "=================")
        file.write(posttext + "\nLink: " + linklist[x] + "\n" + "=================\n")
    pass

def scroll_bottom():
    SCROLL_PAUSE_TIME = 3

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        add_to_list()
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def botting(username, password, page, first, second):
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.delete_all_cookies()

    driver.get('https://www.instagram.com/accounts/login/?next=/' + page + '/')

    time.sleep(4)
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    #login button
    driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button").click()
    time.sleep(3)
    #save login info? - not now
    driver.find_element(By.CSS_SELECTOR, ".sqdOP.yWX7d.y3zKF").click()
    time.sleep(3)
    #scroll then get all posts

    scroll_bottom()

    print(linklist)

    create_data(first, second)

    #closes chrome
    driver.quit()

def botting_captions(username, password, page):
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.delete_all_cookies()

    driver.get('https://www.instagram.com/accounts/login/?next=/' + page + '/')

    time.sleep(4)
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    #login button
    driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button").click()
    time.sleep(3)
    #save login info? - not now
    driver.find_element(By.CSS_SELECTOR, ".sqdOP.yWX7d.y3zKF").click()
    time.sleep(3)
    #scroll then get all posts

    scroll_bottom()

    print(linklist)

    create_data_captions()

    #closes chrome
    driver.quit()

