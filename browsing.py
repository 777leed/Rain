import undetected_chromedriver as uc
from undetected_chromedriver import options

print("Starting")
options = uc.ChromeOptions() 
print("Intializing Arguments")
options.add_argument(r'user-data-dir=C:\Users\hp\AppData\Local\Google\Chrome\User Data')
options.add_argument('--profile-directory=Profile 1')
print("Launching Driver")
driver = uc.Chrome(use_subprocess=True, options=options, driver_executable_path="C:\chromedriver-win64\chromedriver.exe")
print("Starting a Chrome instance...")
driver.get('https://soundcloud.com/')
driver.implicitly_wait(10)
driver.save_screenshot('nowsecure.png')
driver.quit()
