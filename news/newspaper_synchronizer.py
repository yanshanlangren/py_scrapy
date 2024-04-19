# 用Article爬取单条新闻
import newspaper
import time

# 目标新闻网址
url = 'https://cn.nytimes.com/china-ec/'
while True:
    # 构建源
    nyt = newspaper.build(url, language='zh')
    print("新闻数量：%s " % nyt.size())
    # 种类
    # for category in nyt.category_urls():
    #     print(category)

    # 文章
    # for article in nyt.articles:
    #     print(article.url)
    print("sleeping for 1s...")
    time.sleep(1)
