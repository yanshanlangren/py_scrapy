import newspaper
import db.model.news as NewsDAO

# 要同步的新闻地址
urls = {'new_york_times': 'https://cn.nytimes.com'}
max_retry = 3


def sync():
    print("正在同步新闻...")
    for source, url in urls.items():
        sync_website(source, url)
    print("同步完成")


def sync_website(source, url):
    # 构建源
    news_source = newspaper.build(url, language='zh', memoize_articles=False)
    print("新闻数量：%s " % news_source.size())
    # 种类
    # for category in nyt.category_urls():
    #     print(category)

    # 文章
    # for article in nyt.articles:
    #     print(article.url)

    # 下载文章内容
    for article in news_source.articles:
        print("url:%s" % article.url)
        retry = 0
        while retry < max_retry and article.download_state != 2:
            try:
                article.download()
                article.parse()
                NewsDAO.insert(source=source, title=article.title, content=article.text,
                               additional_data=article.additional_data, authors=article.authors, images=article.images,
                               keywords=article.keywords, meta_description=article.meta_description,
                               publish_date=article.publish_date, tags=article.tags,
                               canonical_link=article.canonical_link)
            except Exception as e:
                retry += 1
                print(e)


sync()
