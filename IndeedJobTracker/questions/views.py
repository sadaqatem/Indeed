

# # Create your views here.
# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# import undetected_chromedriver as uc
# # from selenium.webdriver.chrome.options import Options
# # import time
# import sys
# from selenium.common.exceptions import UnexpectedAlertPresentException
# from datetime import datetime, timedelta
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# # from config import config
# from questions.config import *
# import json
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.select import Select
# # Create your views here.
# def sample(request):
#     frequent_questions={}
#     total_jobs_applied=0
#     total_jobs_found=0


#     def element_exists(element):
#         try:
#             WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, element)))
#         except:
#             return False


#     def captcha_check(element='h-captcha'):
#         if element_exists(element) is not False:
#             captcha = driver.find_element_by_class_name(element)
#             if captcha.is_displayed():
#                 print('CAPTCHA has been found')
#                 # winsound.Beep(3000, 1000)
#                 try:
#                     WebDriverWait(driver, long_timeout).until_not(
#                         EC.text_to_be_present_in_element((By.ID, 'login-recaptcha-message-error'),
#                                                         'Captcha validation unsuccessful. Please try again.'))
#                 except:
#                     print('CAPTCHA not solved in time, program terminating\nGood bye')
#                     sys.exit(1)
#                 print('CAPTCHA has been solved')
#             return True
#         else:
#             print('CAPTCHA not found')


#     def popup_check(element='popover-x-button-close'):
#         try:
#             popup_close = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, element)))
#             popup_close.click()
#             print('POPUP has been found\nPOPUP has been closed')
#         except Exception as e:
#             # print('POPUP not found')
#             # print('error: ' + repr(e))
#             pass


#     def next_weekday(date):
#         if date.weekday() in {5, 6}:
#             date += timedelta(days=7 - date.weekday())
#         return date

#     chrome_options=Options()
#     # chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--user-data-dir=c:\\Users\\Sadaqat Khan\\AppData\\Local\\Google\\Chrome\\User Data\\")
#     chrome_options.add_argument('--remote-debugging-port=9222')
#     chrome_options.unexpected_alert_behaviour = "dismiss"
#     chrome_options.add_argument("--no-sandbox") #https://stackoverflow.com/a/50725918/1689770
#     chrome_options.add_argument("--disable-infobars") #https://stackoverflow.com/a/43840128/1689770
#     chrome_options.add_argument("--disable-dev-shm-usage") #https://stackoverflow.com/a/50725918/1689770
#     chrome_options.add_argument("--disable-browser-side-navigation") #https://stackoverflow.com/a/49123152/1689770
#     chrome_options.add_argument("--disable-gpu"); #https://stackoverflow.com/questions/51959986/how-to-solve-selen$
#     chrome_options.add_argument("start-maximized") # https://stackoverflow.com/a/26283818/1689770
#     chrome_options.add_argument("enable-automation") # https://stackoverflow.com/a/43840128/1689770

#     driver = webdriver.Chrome()
#     s = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service = s, options = chrome_options)
#     driver.get(login_url)

#     import json
#     def write_json(data,filename='answers.json'):
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=4)
            
            
            
#     with open('answers.json', encoding='utf-8', errors='ignore') as json_file:
#         data=json.load(json_file, strict=False)  
        
        
#     for job in job_titles: 
#     #     job_postings_url = "https://www.indeed.com/jobs?q=DevOps&l=USA&sc=0kf:attr(DSQF7);&rbl=Remote&fromage=14&vjk=3217b9d9eb0ccdc2"
#         job_postings_url = "https://www.indeed.com/jobs?q=DevOps&l=USA&sc=0kf:attr(DSQF7);&fromage=3&vjk=7fc1660df8945277"
#         try:
#             driver.get(job_postings_url)
#         except UnexpectedAlertPresentException:
#             popup_check()
#             driver.get(job_postings_url)
#             popup_check()
                    
#         job_listing_count = 0
        
#     all_urls=['https://m5.apply.indeed.com/beta/indeedapply/form/resume','https://m5.apply.indeed.com/beta/indeedapply/form/questions/1','https://m5.apply.indeed.com/beta/indeedapply/form/questions/2','https://m5.apply.indeed.com/beta/indeedapply/form/questions/3','https://m5.apply.indeed.com/beta/indeedapply/form/questions/4','https://m5.apply.indeed.com/beta/indeedapply/form/work-experience','https://m5.apply.indeed.com/beta/indeedapply/form/review']
#     pages1=driver.find_elements(By.CSS_SELECTOR,".css-tvvxwd.ecydgvn1 [href]")
#     links1 = [elem.get_attribute('href') for elem in pages1]
#     popup_check()
#     nope=links1.append('https://www.indeed.com/jobs?q=DevOps&l=USA&sc=0kf:attr(DSQF7);&fromage=3&vjk=7fc1660df8945277')
#     print(links1)
#     question_sleep=1
#     ele = links1.pop()
#     for kol in links1:
#         driver.get(kol)
#         popup_check()
#         while True:
#             page_job_links = driver.find_elements(By.CSS_SELECTOR,".jobTitle.css-1h4a4n5.eu4oa1w0 [href]")
#             links = [elem.get_attribute('href') for elem in page_job_links]
#             popup_check()


#             try:
#                 WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Next"]'))).click()
#             except:
#                 break
#         popup_check()
#         for url in links:
#             driver.get(url)
#             popup_check()

#             try:
#             #         if True:
#                 apply_button = driver.find_element(By.CSS_SELECTOR, '.css-1bm49rc.e8ju0x51')
#                 apply_button.click()
#                 total_jobs_found=total_jobs_found+1
#                 time.sleep(5)


#                 for ij in all_urls:
#                     if ij==driver.current_url:
#                         if driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/resume':
#                             popup_check()
#                             print('resume')
#                             time.sleep(5)
#                             driver.find_element(By.ID, 'resume-display-buttonHeader').click()
#                             continue_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ia-continueButton')))
#                             continue_button.click()
#                             time.sleep(5)


#                         elif driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/1' or driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/2' or driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/3' or driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/4' or driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/5':
#                             popup_check()
#                             questions = driver.find_elements(By.CLASS_NAME,'ia-Questions-item')
#                             questions_sleep = 0.25
#                             for question in questions:
#                                 question_1 = question.find_element(By.CSS_SELECTOR,'.css-1ux7cjx.e1wnkr790')

#                                 q_text=question_1.text.lower()

#                                 print(q_text)

#                                 if q_text in data:
#                                     try:
#                                         print('simple blank')
#                                         for i in range(0,5):
#                                             question.find_element(By.CLASS_NAME,'css-anc3lu').send_keys(u'\ue009' + u'\ue003')
                                            
#                                         question.find_element(By.CLASS_NAME,'css-anc3lu').click()
#                                         question.find_element(By.CLASS_NAME,'css-anc3lu').send_keys(data[q_text])
#                                         time.sleep(questions_sleep)
#                                     except:
#                                         try:
#                                             print('blank with arrow')
#                                             for i in range(0,5):
#                                                 question.find_element(By.CSS_SELECTOR,'.css-1ytox4c.e1jgz0i3').send_keys(u'\ue009' + u'\ue003')
#                                             question.find_element(By.CSS_SELECTOR,'.css-1ytox4c.e1jgz0i3').send_keys(data[q_text])
#                                             time.sleep(questions_sleep)
#                                         except:
#                                             try:
#                                                 print('dropdown')
#                                                 question.find_element(By.CSS_SELECTOR,'.css-5mhq3o.eh9h2790').click()
#                                                 question.find_element(By.CSS_SELECTOR,'.css-5mhq3o.eh9h2790').send_keys(data[q_text])
#                                                 time.sleep(questions_sleep)
#                                             except:
#                                                 try:

#                                                     find_q=question.find_element(By.CSS_SELECTOR, "span.css-xex128.e6fjgti0")
#                                                     find_q.find_element(By.TAG_NAME, 'textarea').click()
#                                                     find_q.find_element(By.TAG_NAME, 'textarea').send_keys(data[q_text])
#                                                 except:
#                                                     try:
#                                                         print('radio')
#                                                         btns=question.find_elements(By.CSS_SELECTOR,'.css-d0lawn.es2vvo70')
#                                                         for ik in btns:
#                                                             if ik.text.lower()==data[q_text]:
#                                                                 try:
#                                                                     ik.click()
#                                                                     print('input clicket')
#                                                                     ik.find_element(By.CSS_SELECTOR,'.css-11mq73q.e1rw0n9c1').click()
#                                                                 except:
#                                                                     try:
#                                                                         print('span clicket')
#                                                                         ik.find_element(By.TAG_NAME,'span').click()
#                                                                     except:
#                                                                         ik.find_element(By.CSS_SELECTOR,'.css-11v1v06.e1rw0n9c0').click()
#                                                         time.sleep(1)
#                                                     except:
#                                                         try:
#                                                             print('checkbox')
#                                                             btns=question.find_elements(By.CSS_SELECTOR,'.css-81omu8.es2vvo70')
#                                                             for ik in btns:
#                                                                 if ik.text.lower()==data[q_text]:
#         #                                                             try:
#                                                                     ik.click()
#                                                                     print('input clicket')
#         #                                                             except:
#         #                                                                 try
#                                                                 else:
#                                                                     ik.text.lower()=='not a veteran'
#                                                             time.sleep(1)
#     #                                                 
#     #                                                     
#     #                                                     
#                                                         except Exception as f:
#                                                             print('except error for application button')
#                                                             print('error: ' + repr(f))
#                                 else:
#                                     print('question saved')
#                                     frequent_questions[q_text]=''
                                      
#                                     data[q_text]=''
#                                     write_json(data)
#                                     # frequent_questions.append(data[q_text])


#                             continue_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ia-continueButton')))
#                             continue_button.click()
#                             time.sleep(7)
#                             if driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/1' or driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/2' or driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/3' or driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/4' or driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/5':
#                                 time.sleep(1)
#                                 exit_btn=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/main/div[2]/div[1]/div/div[1]/div[2]/div/button')
#                                 exit_btn.click()
#                                 exit_btn1=driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[3]/button[1]')
#                                 exit_btn1.click()
#                                 print('back click from questions to resume continue loop')

#                         elif driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/work-experience':
#                             popup_check()
#             #                         time.sleep(8)                        
#                             print('experience')
#                             try:
#                                 driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/main/div[2]/div[2]/div/div/div[2]/div/button').click()
#                             except:
#                                 continue_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ia-continueButton')))
#                                 driver.execute_script("arguments[0].style.visibility = 'visible';", continue_button)
#             #                         continue_button.click()
#                                 continue_button.click()
#                             time.sleep(10)
#                             print('Moved from experience page')
#             #                         time.sleep(5)
#             #                         continue
#                         elif driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/review':
#                             popup_check()
#             #                         time.sleep(4)
#                             print('review')

#                             try:
#                                 driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/main/div[2]/div[2]/div/div/div[2]/div/button').click()
#                             except:
#                                 continue_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ia-continueButton')))
#                                 driver.execute_script("arguments[0].style.visibility = 'visible';", continue_button)
#             #                         continue_button.click()
#                                 continue_button.click()
#                             time.sleep(10)
#                             print('Successful Applied')
#                             total_jobs_applied=total_jobs_applied+1

#             except Exception as e:
#                 print('except error for application button')
#                 print('error: ' + repr(e))











#     print('Script completed')
#     # frequent_questions['welcome']=''
    

#     # result_dict=frequent_questions.to_dict('records')
#     return JsonResponse({'Questions':frequent_questions, 'total_jobs_found':total_jobs_found,'total_Jobs_Applied':total_jobs_applied}, status=200)





















































# # Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import pandas as pd

from google.oauth2 import service_account
import sys
from datetime import datetime, timedelta
from IndeedJobTracker.settings import storage_credentials
import time
from questions.config import *
import json

# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.select import Select
# # Create your views here.
# def sample(request):
#     frequent_questions={}
#     total_jobs_applied=0
#     total_jobs_found=0
#     def element_exists(element):
#         try:
#             WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, element)))
#         except:
#             return False


#     def captcha_check(element='h-captcha'):
#         if element_exists(element) is not False:
#             captcha = driver.find_element_by_class_name(element)
#             if captcha.is_displayed():
#                 print('CAPTCHA has been found')
#                 # winsound.Beep(3000, 1000)
#                 try:
#                     WebDriverWait(driver, long_timeout).until_not(
#                         EC.text_to_be_present_in_element((By.ID, 'login-recaptcha-message-error'),
#                                                         'Captcha validation unsuccessful. Please try again.'))
#                 except:
#                     print('CAPTCHA not solved in time, program terminating\nGood bye')
#                     sys.exit(1)
#                 print('CAPTCHA has been solved')
#             return True
#         else:
#             print('CAPTCHA not found')


#     def popup_check(element='popover-x-button-close'):
#         try:
#             popup_close = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, element)))
#             popup_close.click()
#             print('POPUP has been found\nPOPUP has been closed')
#         except Exception as e:
#             # print('POPUP not found')
#             # print('error: ' + repr(e))
#             pass


#     def next_weekday(date):
#         if date.weekday() in {5, 6}:
#             date += timedelta(days=7 - date.weekday())
#         return date

#     chrome_options=Options()
#     # chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--user-data-dir=c:\\Users\\Sadaqat Khan\\AppData\\Local\\Google\\Chrome\\User Data\\")
#     chrome_options.add_argument('--remote-debugging-port=9222')
#     chrome_options.unexpected_alert_behaviour = "dismiss"
#     chrome_options.add_argument("--no-sandbox") #https://stackoverflow.com/a/50725918/1689770
#     chrome_options.add_argument("--disable-infobars") #https://stackoverflow.com/a/43840128/1689770
#     chrome_options.add_argument("--disable-dev-shm-usage") #https://stackoverflow.com/a/50725918/1689770
#     chrome_options.add_argument("--disable-browser-side-navigation") #https://stackoverflow.com/a/49123152/1689770
#     chrome_options.add_argument("--disable-gpu"); #https://stackoverflow.com/questions/51959986/how-to-solve-selen$
#     chrome_options.add_argument("start-maximized") # https://stackoverflow.com/a/26283818/1689770
#     chrome_options.add_argument("enable-automation") # https://stackoverflow.com/a/43840128/1689770

#     driver = webdriver.Chrome()
#     s = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service = s, options = chrome_options)
#     driver.get(login_url)

#     import json
#     def write_json(data,filename='answers.json'):
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=4)
            
            
            
#     with open('answers.json', encoding='utf-8', errors='ignore') as json_file:
#         data=json.load(json_file, strict=False)  
        
        
#     for job in job_titles: 
#     #     job_postings_url = "https://www.indeed.com/jobs?q=DevOps&l=USA&sc=0kf:attr(DSQF7);&rbl=Remote&fromage=14&vjk=3217b9d9eb0ccdc2"
#         job_postings_url = "https://www.indeed.com/jobs?q=DevOps&l=USA&sc=0kf:attr(DSQF7);&fromage=1&vjk=7fc1660df8945277"
#         try:
#             driver.get(job_postings_url)
#         except UnexpectedAlertPresentException:
#             popup_check()
#             driver.get(job_postings_url)
#             popup_check()
                    
#         job_listing_count = 0
        
#     all_urls=['https://m5.apply.indeed.com/beta/indeedapply/form/resume','https://m5.apply.indeed.com/beta/indeedapply/form/questions/1','https://m5.apply.indeed.com/beta/indeedapply/form/questions/2','https://m5.apply.indeed.com/beta/indeedapply/form/questions/3','https://m5.apply.indeed.com/beta/indeedapply/form/questions/4','https://m5.apply.indeed.com/beta/indeedapply/form/work-experience','https://m5.apply.indeed.com/beta/indeedapply/form/review']
#     pages1=driver.find_elements(By.CSS_SELECTOR,".css-tvvxwd.ecydgvn1 [href]")
#     links1 = [elem.get_attribute('href') for elem in pages1]
#     popup_check()
#     nope=links1.append('https://www.indeed.com/jobs?q=DevOps&l=USA&sc=0kf:attr(DSQF7);&fromage=3&vjk=7fc1660df8945277')
#     print(links1)
#     question_sleep=1
#     ele = links1.pop()
#     for kol in links1:
#         driver.get(kol)
#         popup_check()
#         while True:
#             page_job_links = driver.find_elements(By.CSS_SELECTOR,".jobTitle.css-1h4a4n5.eu4oa1w0 [href]")
#             links = [elem.get_attribute('href') for elem in page_job_links]
#             popup_check()


#             try:
#                 WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Next"]'))).click()
#             except:
#                 break
#         popup_check()
#         for url in links:
#             driver.get(url)
#             popup_check()

#             try:
#             #         if True:
#                 apply_button = driver.find_element(By.CSS_SELECTOR, '.css-1bm49rc.e8ju0x51')
#                 apply_button.click()
#                 total_jobs_found=total_jobs_found+1
#                 time.sleep(5)


#                 for ij in all_urls:
#                     if ij==driver.current_url:
#                         if driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/resume':
#                             popup_check()
#                             print('resume')
#                             time.sleep(5)
#                             driver.find_element(By.ID, 'resume-display-buttonHeader').click()
#                             continue_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ia-continueButton')))
#                             continue_button.click()
#                             time.sleep(5)


#                         elif driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/1' or driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/2' or driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/3' or driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/4' or driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/5':
#                             popup_check()
#                             questions = driver.find_elements(By.CLASS_NAME,'ia-Questions-item')
#                             questions_sleep = 0.25
#                             for question in questions:
#                                 question_1 = question.find_element(By.CSS_SELECTOR,'.css-1ux7cjx.e1wnkr790')

#                                 q_text=question_1.text.lower()

#                                 print(q_text)

#                                 if q_text in data:
#                                     try:
#                                         print('simple blank')
#                                         for i in range(0,5):
#                                             question.find_element(By.CLASS_NAME,'css-anc3lu').send_keys(u'\ue009' + u'\ue003')
                                            
#                                         question.find_element(By.CLASS_NAME,'css-anc3lu').click()
#                                         question.find_element(By.CLASS_NAME,'css-anc3lu').send_keys(data[q_text])
#                                         time.sleep(questions_sleep)
#                                     except:
#                                         try:
#                                             print('blank with arrow')
#                                             for i in range(0,5):
#                                                 question.find_element(By.CSS_SELECTOR,'.css-1ytox4c.e1jgz0i3').send_keys(u'\ue009' + u'\ue003')
#                                             question.find_element(By.CSS_SELECTOR,'.css-1ytox4c.e1jgz0i3').send_keys(data[q_text])
#                                             time.sleep(questions_sleep)
#                                         except:
#                                             try:
#                                                 print('dropdown')
#                                                 question.find_element(By.CSS_SELECTOR,'.css-5mhq3o.eh9h2790').click()
#                                                 question.find_element(By.CSS_SELECTOR,'.css-5mhq3o.eh9h2790').send_keys(data[q_text])
#                                                 time.sleep(questions_sleep)
#                                             except:
#                                                 try:

#                                                     find_q=question.find_element(By.CSS_SELECTOR, "span.css-xex128.e6fjgti0")
#                                                     find_q.find_element(By.TAG_NAME, 'textarea').click()
#                                                     find_q.find_element(By.TAG_NAME, 'textarea').send_keys(data[q_text])
#                                                 except:
#                                                     try:
#                                                         print('radio')
#                                                         btns=question.find_elements(By.CSS_SELECTOR,'.css-d0lawn.es2vvo70')
#                                                         for ik in btns:
#                                                             if ik.text.lower()==data[q_text]:
#                                                                 try:
#                                                                     ik.click()
#                                                                     print('input clicket')
#                                                                     ik.find_element(By.CSS_SELECTOR,'.css-11mq73q.e1rw0n9c1').click()
#                                                                 except:
#                                                                     try:
#                                                                         print('span clicket')
#                                                                         ik.find_element(By.TAG_NAME,'span').click()
#                                                                     except:
#                                                                         ik.find_element(By.CSS_SELECTOR,'.css-11v1v06.e1rw0n9c0').click()
#                                                         time.sleep(1)
#                                                     except:
#                                                         try:
#                                                             print('checkbox')
#                                                             btns=question.find_elements(By.CSS_SELECTOR,'.css-81omu8.es2vvo70')
#                                                             for ik in btns:
#                                                                 if ik.text.lower()==data[q_text]:
#         #                                                             try:
#                                                                     ik.click()
#                                                                     print('input clicket')
#         #                                                             except:
#         #                                                                 try
#                                                                 else:
#                                                                     ik.text.lower()=='not a veteran'
#                                                             time.sleep(1)
#     #                                                 
#     #                                                     
#     #                                                     
#                                                         except Exception as f:
#                                                             print('except error for application button')
#                                                             print('error: ' + repr(f))
#                                 else:
#                                     print('question saved')
#                                     frequent_questions[q_text]=''
#                                     data[q_text]=''
#                                     write_json(data)

#                             continue_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ia-continueButton')))
#                             continue_button.click()
#                             time.sleep(7)
#                             if driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/1' or driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/2' or driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/3' or driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/4' or driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/questions/5':
#                                 time.sleep(1)
#                                 exit_btn=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/main/div[2]/div[1]/div/div[1]/div[2]/div/button')
#                                 exit_btn.click()
#                                 exit_btn1=driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[3]/button[1]')
#                                 exit_btn1.click()
#                                 print('back click from questions to resume continue loop')

#                         elif driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/work-experience':
#                             popup_check()
#             #                         time.sleep(8)                        
#                             print('experience')
#                             try:
#                                 driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/main/div[2]/div[2]/div/div/div[2]/div/button').click()
#                             except:
#                                 continue_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ia-continueButton')))
#                                 driver.execute_script("arguments[0].style.visibility = 'visible';", continue_button)
#             #                         continue_button.click()
#                                 continue_button.click()
#                             time.sleep(10)
#                             print('Moved from experience page')
#             #                         time.sleep(5)
#             #                         continue
#                         elif driver.current_url == 'https://m5.apply.indeed.com/beta/indeedapply/form/review':
#                             popup_check()
#             #                         time.sleep(4)
#                             print('review')

#                             try:
#                                 driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/main/div[2]/div[2]/div/div/div[2]/div/button').click()
#                             except:
#                                 continue_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ia-continueButton')))
#                                 driver.execute_script("arguments[0].style.visibility = 'visible';", continue_button)
#             #                         continue_button.click()
#                                 continue_button.click()
#                             time.sleep(10)
#                             print('Successful Applied')
#                             total_jobs_applied=total_jobs_applied+1

#             except Exception as e:
#                 print('except error for application button')
#                 print('error: ' + repr(e))

#     print('Script completed')
#     print('Frequent Questions are',frequent_questions)
#     print('total jobs found are ',total_jobs_found)
#     print('total_Jobs_Applied',total_jobs_applied)
#     # frequent_questions['welcome']=''


#     # result_dict=frequent_questions.to_dict('records')
#     return JsonResponse({'Questions':frequent_questions, 'total_jobs_found':total_jobs_found,'total_Jobs_Applied':total_jobs_applied}, status=200)




from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def show_questions(request):

    SQL_query = f'''
        SELECT
            tb_indeed.questions AS questions,
            tb_indeed.answers AS answers
        FROM
            `earnest-cooler-384808.indeed.questions` AS tb_indeed
        '''
    try:
        print(SQL_query)
        result = pd.read_gbq(SQL_query, credentials=storage_credentials)
        result=result.tail(10)
        result_dict  = result.to_dict('records')
        return JsonResponse({'questions':result_dict}, status=200)

    except Exception as e:
        return JsonResponse({"Error while showing questions and answers data, Error": str(e)}, 
        status=500
        )

@csrf_exempt
def show_jobs(request):

    SQL_query1 = f'''
        SELECT
            tb_jobs.job_title AS job_title,
            tb_jobs.job_location AS job_location,
            tb_jobs.apply_date AS apply_date,
            tb_jobs.job_url AS job_url,
            tb_jobs.apply_status AS apply_status,
        FROM
            `earnest-cooler-384808.indeed.jobs` AS tb_jobs
        '''
    try:
        print(SQL_query1)
        result = pd.read_gbq(SQL_query1, credentials=storage_credentials)
        result=result.tail(10)
        result_dict  = result.to_dict('records')
        return JsonResponse({'jobs':result_dict}, status=200)

    except Exception as e:
        return JsonResponse({"Error while showing jobs data, Error": str(e)}, 
        status=500
        )
    
@csrf_exempt
def show_main(request):

    SQL_query = f'''
        SELECT
            tb_indeed.questions AS questions,
            tb_indeed.answers AS answers
        FROM
            `earnest-cooler-384808.indeed.questions` AS tb_indeed
        '''



    SQL_query1 = f'''
        SELECT
            tb_jobs.job_title AS job_title,
            tb_jobs.job_location AS job_location,
            tb_jobs.apply_date AS apply_date,
            tb_jobs.job_url AS job_url,
            tb_jobs.apply_status AS apply_status,
        FROM
            `earnest-cooler-384808.indeed.jobs` AS tb_jobs
        '''
    try:
        # print(SQL_query1)
        result = pd.read_gbq(SQL_query, credentials=storage_credentials)
        result1 = pd.read_gbq(SQL_query1, credentials=storage_credentials)

        result=result.tail(10)
        result_dict  = result.to_dict('records')

        result1=result1.tail(10)
        result_dict1  = result1.to_dict('records')
        return JsonResponse({'jobs':result_dict1,'questions':result_dict}, status=200)

    except Exception as e:
        return JsonResponse({"Error while showing main page data, Error": str(e)}, 
        status=500
        )