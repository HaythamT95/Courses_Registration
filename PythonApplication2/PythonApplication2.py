from selenium import webdriver

chromewebdriver_location="/Users/hayth/source/repos/PythonApplication2/chromedriver"

driver = webdriver.Chrome(chromewebdriver_location)
driver.get("https://info.braude.ac.il/yedion/fireflyweb.aspx?prgname=login")

#username and password variables and login button paths
username_input="/html/body/main/div[3]/div/div/div/form/div/section/div/div/div/div/div[1]/input"
password_input="/html/body/main/div[3]/div/div/div/form/div/section/div/div/div/div/div[2]/input"
login_submit="/html/body/main/div[3]/div/div/div/form/div/section/div/div/div/div/div[3]/button[1]"

#login page submit information and enter
driver.find_element_by_xpath(username_input).send_keys("Haytham.Taweel")
driver.find_element_by_xpath(password_input).send_keys("Haytham123!")
driver.find_element_by_xpath(login_submit).click()

