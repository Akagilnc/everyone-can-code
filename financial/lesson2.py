from lesson1 import even_or_odd
import pandas as pd
import numpy.random as random
import attr

@attr.s
class Number:
    value = attr.ib()
    even_or_odd = attr.ib(default=None)

def get_numbers():

    number_list = []
    # 设置一组10个随机数字
    for i in random.randint(10000, size=10):
        number = Number(i)

        # 判断其奇偶
        result = even_or_odd(number.value)

        # 记录在每个数字旁边
        number.even_or_odd = result
        number_list.append(number)
    print(number_list)

get_numbers()

class News:
    def __init__(self, news_date, news_content):
        self.news_date = news_date
        self.news_content = news_content

    def __repr__(self):
        return "{}(news_date = {}, news_content = {}) \n".format(
            self.__class__.__name__, self.news_date, self.news_content)

# news_list = []
# df = pd.read_csv('RedditNews.csv')
# for news in df.get_values():
#     news_list.append(News(news[0], news[1]))

# print(news_list)