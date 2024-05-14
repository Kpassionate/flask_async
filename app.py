from flask import Flask

from utils.task import oss_task

app = Flask(__name__)


@app.route('/')
def hello_world():
    oss_task(key='', obj='')
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
