from flask import Flask
from flask_apscheduler import APScheduler
from news.newspaper_synchronizer import sync
import logging

app = Flask(__name__)
app.config.from_pyfile("config.ini")
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(name)s: %(message)s', level=logging.INFO)
scheduler = APScheduler()
Logger = app.logger


@scheduler.task('interval', id='news_sync', seconds=30, misfire_grace_time=900)
def news_sync():
    app.logger.info("调用新闻同步接口")
    sync()


@app.route('/')
def index():
    app.logger.info("调用hello world")
    return "hello world"


if __name__ == '__main__':
    # app.config.from_object(Config())
    # scheduler.init_app(app)
    # scheduler.start()
    app.run(host='0.0.0.0', port=5000)
    # scheduler.init_app(app)
    # scheduler.start()
