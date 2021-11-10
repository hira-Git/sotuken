from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
options = Options()
# options.add_argument('--headless')
driver = webdriver.Chrome('C:\chromedriver',options=options)

run = 1

if run == 0:
    driver.get('https://www.google.co.jp')
    search_bar = driver.find_element_by_name("q")
    search_bar.send_keys("python")
    search_bar.submit()
    for elem_h3 in driver.find_elements_by_xpath('//a/h3'):
        elem_a = elem_h3.find_element_by_xpath('..')  
        print(elem_h3.text)
        print(elem_a.get_attribute('href'))
elif run == 1:
    driver.get('https://jp.mercari.com/item/m65979487099')
    sleep(3)
    error_flg = False
    if error_flg is False:
        try:
            sleep(1)
            start_button = driver.find_element_by_xpath('//button[text()="はじめる"]')
            sleep(1)
            start_button.click()
            sleep(3)
            print(driver.title)
        except Exception:
            print('ログインボタン押下時にエラーが発生しました。')
else:
    driver.get('https://www.mercari.com/jp/u/952517965/')
    search_bar = driver.find_element_by_name("q")
    search_bar.send_keys("python")
    search_bar.submit()
    for elem_h3 in driver.find_elements_by_xpath('//a/h3'):
        elem_a = elem_h3.find_element_by_xpath('..')  
        print(elem_h3.text)
        print(elem_a.get_attribute('href'))
