from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from lesson2_homework import News
import pprint
import time

is_continue = True
options = webdriver.ChromeOptions()
options.headless = True

def get_lastest_new_title():
    lastest_news = ""
    with open('news_file.txt', 'r') as file:
        lastest_news = file.readline()
    return lastest_news.split(" ")[0]

def get_news(browser):
    news_elements_list = browser.find_elements_by_css_selector('body > div:nth-child(7) > div.box835.hidden.left > ul > li')
    result_list = []
    for news_element in news_elements_list:
        news = News(title=news_element.find_element_by_tag_name('a').text, autho='', source=page_link, link=news_element.find_element_by_tag_name('a').get_attribute('href'),
                    public_time=news_element.find_element_by_tag_name('span').text, is_read=False, content='')
        if news.title == get_lastest_new_title():
            is_continue = False
            break
        result_list.append(news)

    return result_list

def write_news(result_list):
    with open('news_file.txt', 'r') as file:
        all_news = file.readlines()[:-1]

    with open('news_file.txt', 'w') as file:
        for news in result_list:
            print(news.title)
            file.write(news.title + " " + news.public_time + " " + news.link + '\n')
        file.writelines(all_news)


page_link = 'http://www.cs.com.cn/ssgs/gsxw/'
browser = webdriver.Chrome('./chromedriver', options=options)
browser.get(page_link)
result_list = get_news(browser)
# while True:
page_element_list = browser.find_elements_by_css_selector('body > div:nth-child(7) > div.box835.hidden.left > div.page > a')
#     next_page_element = page_element_list[-1]
#     if next_page_element.text != '下一页':
#         break
#     next_page_element.click()
link_list = [page_element.get_attribute('href') for page_element in page_element_list]
link_list = link_list[:-1]
for link in link_list[:2]:
    browser.get(link)
    if is_continue: 
        temp_list = get_news(browser)
        result_list += temp_list


write_news(result_list)
