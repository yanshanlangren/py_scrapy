# py_scrapy

## 写在开始前
这一切开始于假设：<b>全知意味着全能</b>

如果我们知道雨水是由云层形成的

如果我们知道我们的头上有一片很厚的乌云

那么在以前人们很难以想象的气象预测就变成了可能

如果我们知道股票的变化是由公司的运营情况,政策,战争,利率等因素影响

我们是不是可以预测股票的变化从而获利?

即使预测得不是那么准确,是不是可以比当前只通过分析公司运营情况数据更准确一些?



## 大概想法

### py_scrapy ### 

这是一个爬虫项目, 用来爬取很多可靠新闻网站的新闻, 使用结构化的数据存储于数据库中.

爬取股票网站中的股票变化数据存储于数据库中.

### project_data_cleaner ###

用于清洗数据, 过滤无效的数据

将新闻,政策等信息运用nlp(自然语言处理)和信息提取技术,转化成结构化数据标签作为影响因素.

### project_analysis ###

使用ai算法(神经网络/大模型之类的)对影响因素数据和股票变化数据训练成模型.

同时,预测未来的股票走势



## 一些细节 ##

暂时先不写了





