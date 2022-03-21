from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromewebdriver_location="/Users/hayth/source/repos/PythonApplication2/chromedriver.exe"

opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:8080")
driver=webdriver.Chrome(chromewebdriver_location,chrome_options=opt)
wait = WebDriverWait(driver,20)
driver.switch_to.window(driver.current_window_handle)

#click on register courses tab
def chooseCourses():
    chooseTab="/html/body/div/div[1]/div/div/div/div[3]/div/div/div/div/div[8]"
    chooseCourses="/html/body/div/div[1]/div/div/div/div[3]/div/div/div/div/div[8]/div/div[1]/a"
    driver.find_element_by_xpath(chooseTab).click()
    driver.find_element_by_xpath(chooseCourses).click()

#input course number
def inputCourseNum(courseNum):
    courseNumberPath="/html/body/div/div[3]/div/div/div[2]/div/div/div/form/div[2]/table/tbody/tr[2]/td[3]/input"
    driver.find_element_by_xpath(courseNumberPath)
    driver.find_element_by_xpath(courseNumberPath).click()
    driver.find_element_by_xpath(courseNumberPath).send_keys(courseNum)
    #find course
    btnSearch="/html/body/div/div[3]/div/div/div[2]/div/div/div/form/div[2]/table/tbody/tr[8]/td/input[2]"
    driver.find_element_by_xpath(btnSearch).click()


#register to lecture & tergol & lab
def registerToLectures(path):
    button = driver.find_element_by_xpath(path)
    driver.execute_script("arguments[0].click();", button)

chooseCourses()
inputCourseNum("61767") #crypto
#crypto paths
lecturePath="/html/body/div/div[3]/div/div/div[2]/div/div/div/form/div/div[2]/div[1]/div/a[1]"
tergolPath="/html/body/div/div[3]/div/div/div[2]/div/div/div/form/div/div[2]/div[3]/div/a[1]"
registerToLectures(lecturePath)
chooseCourses()
inputCourseNum("61767") #crypto
registerToLectures(tergolPath)

chooseCourses()
inputCourseNum("61758") #Operating systems & real time
#Operating systems & real time paths
lecturePath="/html/body/div/div[3]/div/div/div[2]/div/div/div/form/div/div[2]/div[1]/div/a[1]"
labPath="/html/body/div/div[3]/div/div/div[2]/div/div/div/form/div/div[2]/div[3]/div/a[1]"
tergolPath="/html/body/div/div[3]/div/div/div[2]/div/div/div/form/div/div[2]/div[9]/div/a[1]"
registerToLectures(lecturePath)
chooseCourses()
inputCourseNum("61758") #Operating systems & real time
registerToLectures(labPath)
chooseCourses()
inputCourseNum("61758") #Operating systems & real time
registerToLectures(tergolPath)

chooseCourses()
inputCourseNum("61761") #Data mining & AI
#Data mining & AI paths
lecturePath="/html/body/div/div[3]/div/div/div[2]/div/div/div/form/div/div[2]/div[1]/div/a[1]"
tergolPath="/html/body/div/div[3]/div/div/div[2]/div/div/div/form/div/div[2]/div[5]/div/a[1]"
registerToLectures(lecturePath)
chooseCourses()
inputCourseNum("61761") #Data mining & AI
registerToLectures(tergolPath)


chooseCourses()
inputCourseNum("61764") #graphics
#graphics paths
lecturePath="/html/body/div/div[3]/div/div/div[2]/div/div/div/form/div/div[2]/div[2]/div/a[1]"
labPath="/html/body/div/div[3]/div/div/div[2]/div/div/div/form/div/div[2]/div[3]/div/a[1]"
registerToLectures(lecturePath)
chooseCourses()
inputCourseNum("61764") #graphics
registerToLectures(labPath)

chooseCourses()
inputCourseNum("61763") #compilation
#compilation paths
lecturePath="/html/body/div/div[3]/div/div/div[2]/div/div/div/form/div/div[2]/div[2]/div/a[1]"
tergolPath="/html/body/div/div[3]/div/div/div[2]/div/div/div/form/div/div[2]/div[3]/div/a[1]"
registerToLectures(lecturePath)
chooseCourses()
inputCourseNum("61763") #compilation
registerToLectures(tergolPath)
