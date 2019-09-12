from selenium import webdriver
import pyautogui as gui

name = gui.prompt('Enter Target Name')
msg = gui.prompt("Enter Message")
count = int(gui.prompt("Number of Message"))

driver = webdriver.Chrome(executable_path=r'C:/Program Files/chromedriver.exe')
driver.get('https://web.whatsapp.com')

con = gui.confirm('Are you scanned the QR')
if con == 'OK':
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click()
    msg_box = driver.find_element_by_class_name('_3u328')
    for i in range(count):
        msg_box.send_keys(msg)
        btn = driver.find_element_by_class_name('_3M-N-').click()
P6z4j