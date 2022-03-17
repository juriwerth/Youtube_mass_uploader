# Code by Juri Werth ---> https://github.com/juriwerth
# Selenium bot that uploads many youtube vidoes a day!

#############################################################################################################################
# Imports

from selenium import webdriver
import random
import time

from credentials import *

#############################################################################################################################
# Declarations

counter = 0

# Arrays for the ransomizer
rl50 = []
rl2000 = []

#############################################################################################################################
# Uploader

def bot():

    # Randomize delays
    for i in range(0,30):
        n = random.randint(0,50)
        rl50.append(n)

    for i in range(0,30):
        n = random.randint(1000,2000)
        rl2000.append(n)

    rl = [i / j for i, j in zip(rl50, rl2000)]

# Add more choises in the emailinput if you have multiple emails and add more elifs

    emailinput = input('\nChoose your email:\n1: '+EMAILS[0]+'\nIf your email isnt in this list, just enter your email')

    if emailinput == '1':
        EMAIL = EMAILS[0]
    else:
        EMAIL = emailinput

    print('Logging in as '+EMAIL)

    videoinput = input('\nChoose your video:\n1: The name of your video\nr: Random')

    if videoinput == '1':
        VIDEO = VIDEO1
        print('VIDEO: The name of your video')

# If you have added more videos and add it in the randomizer down below

    elif videoinput == 'r':
        VIDEO = random.choice(VIDEO[0])
        print('Random: '+VIDEO)

    headlessinput = input('\nHeadless:\n(y/n)\n')

    if headlessinput == 'y':
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
    else:
        options = webdriver.ChromeOptions()

    # Starting the driver
    driver = webdriver.Chrome(executable_path='C:/Users/juriw/OneDrive/Desktop/42/coding/projects/py/yt_uploadbot/chromedriver.exe', options=options)
    driver.get('https://youtube.com/')
    time.sleep(1+rl[0])
    
    driver.find_element_by_xpath('/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[3]/div[2]/div[2]/ytd-button-renderer/a/tp-yt-paper-button').click()
    time.sleep(2+rl[1]) 
    
    # Password input
    emailinput = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
    time.sleep(rl[2])
    emailinput.send_keys(EMAIL)
    time.sleep(2+rl[3])
    
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
    time.sleep(3+rl[4])
     
    # Password input
    passinput = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    time.sleep(rl[5])
    passinput.send_keys(PASS)
    time.sleep(2+rl[6])
     
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
    time.sleep(3+rl[7])
    
    driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-topbar-menu-button-renderer[3]/button/yt-img-shadow/img').click()
    time.sleep(2+rl[8])

    driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a/tp-yt-paper-item').click()
    time.sleep(3+rl[9])
    
    def loop():

        global counter

        # Upload video button
        driver.find_element_by_xpath('/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[1]/div[1]/ytcp-quick-actions/a[1]/ytcp-icon-button').click()
        time.sleep(2+rl[10])
        
        # Uplaoding video
        driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/input').send_keys(VIDEO[0])
        time.sleep(10+rl[11])
        
        # Video titel
        driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-mention-input/div').send_keys(VIDEO[1])
        time.sleep(3+rl[12])
        
        # Video discription
        driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-mention-input/div').send_keys(VIDEO[2])
        time.sleep(1+rl[13])

        # Done button
        driver.find_element_by_xpath('/html/body/ytcp-playlist-dialog/tp-yt-paper-dialog/div[2]/ytcp-button[3]').click()
        time.sleep(1+rl[16])

        # Next button
        driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]').click()
        time.sleep(1+rl[17])
        
        # Next button
        driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]').click()
        time.sleep(1+rl[18])
        
        # Next button
        driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]').click()
        time.sleep(1+rl[19])
        
        # Setting the video public
        driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]').click()
        time.sleep(1+rl[20])
        
        # Publishing the video
        driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]').click()
        time.sleep(5+rl[21])

        
        driver.refresh()
    
        counter += 1
        strcounter = str(counter)
        print('Videos posted: '+strcounter+' on '+EMAIL)

        time.sleep(3+rl[22])

        loop()

    loop()
    driver.quit()

bot()