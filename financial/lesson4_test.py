from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pprint import pprint

options = Options()
options.headless = True

page_link = 'http://www.cs.com.cn/ssgs/gsxw/'
driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.get(page_link)

# news_titles = driver.find_elements_by_class_name('mEaVNd')
news_list = driver.find_elements_by_css_selector('body > div:nth-child(7) > div.box835.hidden.left > ul > li')

# pprint([news.text for news in news_list])
pprint([(news.find_element_by_tag_name('span').text, news.find_element_by_tag_name('a').get_attribute('href'),
         news.find_element_by_tag_name('a').text) for news in news_list])
