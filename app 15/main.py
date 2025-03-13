from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

class WebAutomation:
    def __init(self):

        chrome_options = Options()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--allow-running-insecure-content")

        #setting path for downloads
        download_path = os.getcwd()
        prefs ={'download.default_directory':download_path}
        chrome_options.add_experimental_option('prefs',prefs)

        service_obj = Service('chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(options=chrome_options,service=service_obj)

    def login(self,username,password):
        self.driver.get("https://demoqa.com/login")

        user_name = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'userName')))
        password_feild = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'password')))
        login_button = self.driver.find_element(By.ID,'login')

        user_name.send_keys(username)
        password_feild.send_keys(password)
        self.driver.execute_script('arguments[0].click();',login_button)

    def locate(self,name,email_id,current_address,permanent_address):

        #locate element drop down
        elements = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        elements.click()

        #locate text box
        text_box = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'item-0')))
        text_box.click()

        #locate element
        full_name = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'userName')))
        email = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'userEmail')))
        cur_address = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'currentAddress')))
        per_address = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'permanentAddress')))
        submit_button = self.driver.find_element(By.ID,'submit')

        #filling form
        full_name.send_keys(name)
        email.send_keys(email_id)
        cur_address.send_keys(current_address)
        per_address.send_keys(permanent_address)

        self.driver.execute_script('arguments[0].click();',submit_button)

    def download(self):

        #locate download
        download_feild = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'item-7')))
        download_feild.click()

        #download 
        download = self.driver.find_element(By.ID,'downloadButton')
        self.driver.execute_script('arguments[0].click();',download)

    def close(self):
        self.driver.quit()

if __name__ =="__main__":
    web = WebAutomation()
    web.login()
    web.locate()
    web.download()
    web.close()
