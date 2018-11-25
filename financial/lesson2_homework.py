# 实现一个News的类，
class News:
    # 其属性包括 标题，作者，来源，链接，发布时间，是否已读
    def __init__(self, title, autho, source, link, public_time, is_read, content):
        self.title = title
        self.autho = autho
        self.source = source
        self.link = link
        self.public_time = public_time
        self.is_read = is_read
        self.content = content
        self.keyword = self.get_keyword(content)

    # 实现一个类里的函数，调用将新闻的未读已读状态改变
    def change_read(self):
        self.is_read = not self.is_read

    # 搜索关键字
    def get_keyword(self, content):
        index_start = 0
        keyword = ''
        while True:
            # 找到第一个关键字
            index = content.find("价格", index_start)

            # 如果找到了
            if index != -1:
                keyword += content[index:content.find(',', index)] + '; '
                # 下一次搜索的时候，起点要往后移动一位
                index_start = index + 1
            # 如果没找到
            if index == -1:
                return keyword


# 写3条以上的测试数据，把News对象放到一个News_list里面，
eduction_news = News("kids programming", 'ak', 'yahoo', 'http://1.com', "2018.11.23 13:00:00", False, "dfadfdasfdadfds, 价格 10000, balslbals")
kids_news = News("kids", 'ak', 'yahoo', 'http://2.com', "2018.11.24 13:00:00", False, "价格2 20000, dafdfasdfda, 价格1 10000")
coding_news = News("kids coding", 'ak', 'yahoo', 'http://3.com', "2018.11.25 13:00:00", False, "afdfdsfdsfda, cont 3000, dfadfadf")
news_list = [eduction_news, kids_news, coding_news]

# 并且至少调用一次改变已读或未读的函数
kids_news.change_read()
coding_news.change_read()

# 实现一个调用函数，依次取出News_list里的所有News，并展示其 标题，作者，来源，链接，发布时间和是否已读
for news in news_list:
    print(news.title, news.keyword)



