import pyautogui as bot
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import random
import time

# Set path to your webdriver
driver = webdriver.Chrome("PATH_TO_YOUR_WEBDRIVER")
wait = WebDriverWait(driver, 100)


def user_login():
    # Replace with your login details
    user_email = 'YOUR_FLICKR_EMAIL'
    user_password = 'YOUR_FLICKR_PASSWORD'
    driver.maximize_window()
    driver.get("https://www.flickr.com/login")
    print("Signing in.")
    username = driver.find_element(By.CSS_SELECTOR, "#login-email")
    username.click()
    username.send_keys(user_email)
    print("Email entered.")
    next_button = driver.find_element(By.CSS_SELECTOR, "#login-form > button")
    next_button.click()
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "#login-password")))
    password = driver.find_element(By.CSS_SELECTOR, "#login-password")
    password.click()
    password.send_keys(user_password)
    print("Password entered.")
    sign_in = driver.find_element(By.CSS_SELECTOR, "#login-form > button")
    sign_in.click()
    print("Signed in successfully. Proceeding with next task.")
    WebDriverWait(driver, 15).until(ec.presence_of_element_located((By.CLASS_NAME, "count-text")))


user_login()


def find_image():
    # Replace with the link to the image you want to interact with
    image_link = 'https://flickr.com/photos/YOUR_PHOTO_ID/'
    driver.get(image_link)
    print("Image found. Proceeding with next task.")


find_image()

list_wait = list(range(1,11))


def interact():
    # Replace with your list of comments
    comment_list = ['YOUR_LIST_OF_COMMENTS']
    bot.click(1690, 200)  # Clicks on a specific position on the screen
    bot.hotkey("f")  # Presses the 'f' key
    bot.hotkey("c")  # Presses the 'c' key
    bot.typewrite(random.choice(comment_list))  # Types a random comment from the list
    bot.keyDown('ctrl')
    bot.hotkey('enter')  # Presses the 'Enter' key
    bot.keyUp('ctrl')
    bot.hotkey("right")  # Presses the 'Right' arrow key
    time.sleep(2)  # Waits for 2 seconds


interact()

loops = 0
while loops < 50000:
    interact()
    loops = loops + 1
    print(loops)
    bot.hotkey("escape")  # Presses the 'Escape' key
    bot.hotkey("f5")  # Presses the 'F5' key (Refresh)
    bot.hotkey("enter")  # Presses the 'Enter' key
    time.sleep(1)  # Waits for 1 second
