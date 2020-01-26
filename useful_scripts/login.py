from selenium.webdriver.support.select import Select
import time
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options=Options()
options.headless=False
driver = webdriver.Chrome(executable_path='/home/control/chromedriver',options=options)

driver.get('https://iac.srmist.edu.in/connect/PortalMain')
adv= driver.find_element_by_id('details-button')
adv.click()
proc= driver.find_element_by_id('proceed-link')
proc.click()
time.sleep(5)
user=driver.find_element_by_id('LoginUserPassword_auth_username')
pswd=driver.find_element_by_id('LoginUserPassword_auth_password')
user.send_keys('username')
pswd.send_keys('password')
sub_box= driver.find_element_by_id('UserCheck_Login_Button_span')
sub_box.click()
time.sleep(5)
driver.quit()


