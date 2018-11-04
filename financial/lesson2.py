from financial.lesson1 import even_or_odd
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
    print(number_list, '\n')


@attr.s
class News:
    news_date = attr.ib()
    news_content = attr.ib()


get_numbers()
news_list = []
df = pd.read_csv('RedditNews.csv')
for news in df.get_values():
    news_list.append(News(news[0], news[1]))

print(news_list)
