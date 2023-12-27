import requests
import time,io
from PIL import Image
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from getpass import getpass

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def login(driver,username,password):
    driver.get('https://studentportal.hindustanuniv.ac.in/home.htm')
    driver.find_element(By.XPATH, '//*[@id="username_temp"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="form-password"]').send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/form/button').click()
    print('LOGGED IN...')
    
def take_long_screenshot(driver, filename):
    driver.get("https://studentportal.hindustanuniv.ac.in/search/attendanceStatus.htm")
    total_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1920, total_height)
    stitched_image = Image.new("RGB", (1920, total_height))
    offset = 0
    while offset < total_height:
        driver.execute_script(f"window.scrollTo(0, {offset});")
        time.sleep(1)
        screenshot = driver.get_screenshot_as_png()
        screenshot = Image.open(io.BytesIO(screenshot))
        stitched_image.paste(screenshot, (0, offset))
        offset += screenshot.size[1]
    stitched_image.save(filename)
    print(f"Long screenshot saved as {filename}")

username = input('Enter your username:- ')
password = getpass('Enter your password:- ')

login(driver,username,password)
take_long_screenshot(driver,'temp.png')

driver.quit()



(_TOKEN)='6452299450:AAEEzwh9EH8CjFqme78aQ79kYnMt8xVwxxU'


def send_photo(chat_id, image_path, image_caption="hi"): 
     data = {"chat_id": 1145627639, "caption": image_caption} 
     url = f'https://api.telegram.org/bot{_TOKEN}/sendPhoto' 
     with open(image_path, "rb") as temp: 
         rek = requests.post(url, data=data, files={"photo": temp}) 
         print(rek.text) 
     return rek.json()
send_photo(1145627639,'temp.png','attendance status')



def send_msg(text):
    token = "6452299450:AAEEzwh9EH8CjFqme78aQ79kYnMt8xVwxxU"
    chat_id = "1145627639"
    
    results = url_req = "https://api.telegram.org/bot"+ token +"/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    requests.get(url_req)
    return results.json()
    
send_msg("hi naveen akash here your attendance")