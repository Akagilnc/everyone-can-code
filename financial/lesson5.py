from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from lesson2_homework import News
import time

options = webdriver.ChromeOptions()
options.headless = True

page_link = 'http://www.cs.com.cn/ssgs/gsxw/'
browser = webdriver.Chrome('./chromedriver', options=options)
browser.get(page_link)


def get_news(browser):
    news_elements_list = browser.find_elements_by_css_selector('body > div:nth-child(7) > div.box835.hidden.left > ul > li')
    return [news.text for news in news_elements_list]

# news_element.find_element_by_tag_name('a').click()
# browser.switch_to.window(browser.window_handles[1])

def get_content(browser): 
    contents_element = browser.find_element_by_css_selector('body > div:nth-child(9) > div.box835.hidden.left > div.article > div.article-t.hidden > div.Custom_UnionStyle > div')
    return contents_element.text


# get_content(browser)
page_elements_list = browser.find_elements_by_css_selector('body > div:nth-child(7) > div.box835.hidden.left > div.page > a')
news_elements_list = get_news(browser)
page_link_set = set([page.get_attribute('href') for page in page_elements_list])
for link in page_link_set:
    print(link)
    browser.get(link)
    news_elements_list.append(get_news(browser))
print(news_elements_list)
browser.quit()