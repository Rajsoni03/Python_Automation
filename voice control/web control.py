import pyaudio
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pyttsx3
from time import sleep
import pyautogui as pui


fb_id = 'your id'
fb_pass = 'your pass'

r = sr.Recognizer()
engine = pyttsx3.init()
driver = webdriver.Chrome(executable_path=r'C:/Program Files/chromedriver.exe')

like_cls = '_6rk2 img sp_S8pk_WlQaUU sx_c69f09'

engine.say('Hello Sir, I am Atlas')
engine.say('Your Laptop is ready for use')
engine.runAndWait()

while True:
    with sr.Microphone() as source:
        print('start')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            if text =='open my Facebook' or text == 'open Facebook':
                driver = webdriver.Chrome(executable_path=r'C:/Program Files/chromedriver.exe')
                driver.get('https://www.facebook.com/')
                engine.say('Facebook is ready to use, Please login sir')
                engine.runAndWait()
            elif text == 'login my account':
                engine.say('Sure Sir')
                engine.runAndWait()
                driver.find_element_by_id('email').send_keys(fb_id)
                driver.find_element_by_id('pass').send_keys(fb_pass)
                driver.find_element_by_id('loginbutton').click()
                engine.say('Your FaceBook Account is Successfullly login')
                engine.say('Now What Sir')
                engine.runAndWait()
            elif text == 'open notification':
                engine.say('sure sir')
                engine.runAndWait()
                driver.find_element_by_class_name('_2n_9 f_click').click()
            elif text == 'mark all as read':
                engine.say('are ou sure sir')
                engine.runAndWait()
                audio = r.listen(source)
                try:
                    text = str(r.recognize_google(audio)).title()
                    if text == 'yes' or text == 'yes i am sure':
                        driver.find_element_by_id('u_0_j').click()
                        engine.say('done sir')
                        engine.runAndWait()
                except:
                    pass
            elif text == 'open my WhatsApp' or text == 'open WhatsApp':
                engine.say('Okay Sir')
                engine.runAndWait()
                driver.get('https://web.whatsapp.com')
                engine.say('Sir, WhatsApp is ready for use, Please Scan QR from Your Mobile')
                engine.runAndWait()
            elif text=='send a message' or text=='messege':
                engine.say('Okay Sir')
                engine.say('Who do you want to send the message.')
                engine.runAndWait()
                audio = r.listen(source)
                try:
                    name = str(r.recognize_google(audio))
                    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name.title())).click()
                    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click()
                    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click()
                    engine.say('What Message you want to send')
                    engine.runAndWait()
                    audio = r.listen(source)
                    try:
                        msg = str(r.recognize_google(audio)).title()
                        msg_box = driver.find_element_by_class_name('_3u328')
                        msg_box.send_keys(msg)
                        btn = driver.find_element_by_class_name('_3M-N-').click()
                        engine.say('Message is sended to {}'.format(name))
                        engine.runAndWait()
                    except:
                        print('error')
                except:
                    engine.say('Anything Else Sir')
                    engine.runAndWait()
            elif text=='type' or text=='type a message' or text=='type message':
                engine.say('Okay Sir')
                engine.runAndWait()
                sleep(.5)
                audio = r.listen(source)
                try:
                    msg = str(r.recognize_google(audio)).title()
                    msg_box = driver.find_element_by_class_name('_3u328')
                    msg_box.send_keys(msg)
                    btn = driver.find_element_by_class_name('_3M-N-').click()
                    engine.say('Message is send')
                    engine.runAndWait()
                except:
                    pass

            elif text == 'delete' or text == 'delete message':
                engine.say('are you sure, sir')
                engine.runAndWait()
                audio = r.listen(source)

                try:
                    temp_ans = str(r.recognize_google(audio))
                    if temp_ans == 'yes':
                        lastmsg = driver.find_elements_by_class_name('-N6Gq')[-1]
                        ActionChains(driver).move_to_element(lastmsg).perform()
                        print("a")
                        driver.find_element_by_class_name('_2-qoA').click()
                        print("b")
                        driver.find_element_by_xpath('//div[@title = "Delete message"]').click()
                        print('c')
                        try:
                            driver.find_elements_by_xpath("//*[contains(text(), 'Delete for everyone')]")
                            # driver.find_elements_by_class_name('_2eK7W _23_1v')[-1].click()
                            driver.find_element_by_class_name('_2eK7W _3PQ7V').click()
                        except:
							driver.find_elements_by_xpath("//*[contains(text(), 'Delete for me')]")
							# driver.find_element_by_class_name('_2eK7W _3PQ7V').click()

                        engine.say('Message is deleted')
                        engine.runAndWait()
                    else:
                        engine.say('okay, sir')
                        engine.runAndWait()
                except:
                    print('error')
                    pass

            elif text == 'shutdown' or text == 'stop jarvis':
                engine.say('I am Off')
                engine.runAndWait()
                break
            elif text != '':
                engine.say("Sorry Sir, i con't recognize your voice")
                engine.runAndWait()
        except:
            pass