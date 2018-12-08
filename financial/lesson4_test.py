from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from lesson2_homework import News

options = Options()
options.headless = True

page_link = 'http://www.cs.com.cn/ssgs/gsxw/'
browser = webdriver.Chrome('./chromedriver', chrome_options=options)
browser.get(page_link)

news_elements_list = browser.find_elements_by_css_selector('body > div:nth-child(7) > div.box835.hidden.left > ul > li')


result_list = []
for news_element in news_elements_list:
    news = News(title=news_element.find_element_by_tag_name('a').text, autho='', source=page_link, link=news_element.find_element_by_tag_name('a').get_attribute('href'),
                public_time=news_element.find_element_by_tag_name('span').text, is_read=False, content='')
    result_list.append(news)

with open('news_file.txt', 'w') as file:
    for news in result_list:
        file.write(news.title + " " + news.public_time + " " + news.link + '\n')



