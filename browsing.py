import undetected_chromedriver as uc
from undetected_chromedriver import options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC  # noqa
from selenium.webdriver.support.wait import WebDriverWait
import time

# driver.save_screenshot('nowsecure.png')


def scroll_down(driver):
    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height

def getFollow(username):
    print("Starting")
    options = uc.ChromeOptions() 
    print("Intializing Arguments")
    options.add_argument(r'user-data-dir=C:\Users\hp\AppData\Local\Google\Chrome\User Data')
    options.add_argument('--profile-directory=Profile 1')
    print("Launching Driver")
    driver = uc.Chrome(headless=True,use_subprocess=True, options=options, driver_executable_path="C:\chromedriver-win64\chromedriver.exe")
    print("Starting a Chrome instance...")
    driver.implicitly_wait(10)
    print("Navigating to follower's page")
    driver.get(f'https://soundcloud.com/{username}/followers')
    scroll_down(driver)
    print("Collecting Users who follow you")
    followers =  driver.find_elements(By.CLASS_NAME, 'userBadgeListItem__heading')
    iNeedNames = []
    for follower in followers :
        iNeedNames.append(follower.get_attribute('innerHTML').strip())
    driver.close()

    return iNeedNames

def getFollowing(username):
    print("Starting")
    options = uc.ChromeOptions() 
    print("Intializing Arguments")
    options.add_argument(r'user-data-dir=C:\Users\hp\AppData\Local\Google\Chrome\User Data')
    options.add_argument('--profile-directory=Profile 1')
    print("Launching Driver")
    driver = uc.Chrome(headless=True,use_subprocess=True, options=options, driver_executable_path="C:\chromedriver-win64\chromedriver.exe")
    print("Starting a Chrome instance...")
    driver.implicitly_wait(10)
    print("Navigating to following page")
    driver.get('https://soundcloud.com/777-leed/following')
    scroll_down(driver)
    print("Collecting Users you are following")
    following =  driver.find_elements(By.CLASS_NAME, 'userBadgeListItem__heading')
    iNeedNames = []
    for follower in following :
        iNeedNames.append(follower.get_attribute('innerHTML').strip())    
    return iNeedNames

def getFollowingWithDriver(driver):
    print("Navigating to following page")
    driver.get('https://soundcloud.com/777-leed/following')
    scroll_down(driver)
    print("Collecting Users you are following")
    following =  driver.find_elements(By.CLASS_NAME, 'userBadgeListItem__heading')
    iNeedNames = []
    for follower in following :
        iNeedNames.append(follower.get_attribute('innerHTML').strip())    
    return iNeedNames

def getFollowersWithDriver(driver):
    print("Navigating to followers page")
    driver.get('https://soundcloud.com/777-leed/followers')
    scroll_down(driver)
    print("Collecting Users that follow you")
    following =  driver.find_elements(By.CLASS_NAME, 'userBadgeListItem__heading')
    iNeedNames = []
    for follower in following :
        iNeedNames.append(follower.get_attribute('innerHTML').strip())    
    return iNeedNames



def whoIsNotFollowingYouBack(list1, list2):

    set1 = set(list1)
    missing_elements = [element for element in list2 if element not in set1]
    return missing_elements

def getImposters():
    print("Starting")
    options = uc.ChromeOptions() 
    print("Intializing Arguments")
    options.add_argument(r'user-data-dir=C:\Users\hp\AppData\Local\Google\Chrome\User Data')
    options.add_argument('--profile-directory=Profile 1')
    print("Launching Driver")
    driver = uc.Chrome(headless=True,use_subprocess=True, options=options, driver_executable_path="C:\chromedriver-win64\chromedriver.exe")
    print("Starting a Chrome instance...")
    driver.implicitly_wait(10)
    fol = getFollowersWithDriver(driver)
    folw = getFollowingWithDriver(driver)
    imp = whoIsNotFollowingYouBack(fol,folw)
    return imp




# print("Starting")
# options = uc.ChromeOptions() 
# print("Intializing Arguments")
# options.add_argument(r'user-data-dir=C:\Users\hp\AppData\Local\Google\Chrome\User Data')
# options.add_argument('--profile-directory=Profile 1')
# print("Launching Driver")
# driver = uc.Chrome(headless=True,use_subprocess=True, options=options, driver_executable_path="C:\chromedriver-win64\chromedriver.exe")
# print("Starting a Chrome instance...")
# driver.implicitly_wait(10)
# followers = getFollow(driver)
# following = getFollowing(driver)
# imposters = whoIsNotFollowingYouBack(followers,following)
# print("You got " + str(len(followers))+ ' followers')
# print("You are following " + str(len(following))+ ' ppl')
# print("These users are not following you back: "+ str(imposters))
# unfollowImposters(driver)

print(getFollow('777-leed'))










