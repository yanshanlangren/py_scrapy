from flask import Flask
from flask_apscheduler import APScheduler


class Config(object):
    SCHEDULER_API_ENABLED = True


app = Flask(__name__)

scheduler = APScheduler()


@scheduler.task('interval', id='news_sync', seconds=30, misfire_grace_time=900)
def news_sync():
    print("123")


@app.route('/')
def index():
    return "hello world"


if __name__ == '__main__':
    app.config.from_object(Config())
    scheduler.init_app(app)
    scheduler.start()
    app.run()
