from flask import Flask
from flask_apscheduler import APScheduler
from news.newspaper_synchronizer import sync
import logging

# class Config(object):
#     SCHEDULER_API_ENABLED = True


app = Flask(__name__)
app.config.from_pyfile("config.ini")
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(name)s: %(message)s', level=logging.INFO)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
app.run(host='0.0.0.0', port=8000)


@scheduler.task('interval', id='news_sync', seconds=300, misfire_grace_time=900)
def news_sync():
    # print("123")
    app.logger.info("调用新闻同步接口")
    sync()


@app.route('/')
def index():
    app.logger.info("调用hello world")
    return "hello world"
