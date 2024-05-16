from flask import Flask, request, jsonify
from utils.task import oss_task

app = Flask(__name__)


@app.route('/')
def hello_world():
    oss_task(key='', obj='')
    return 'Hello World!'


@app.route("/upload", methods=["GET", "POST"])
def upload_files():
    data = request.form
    file_name = data.get('file_name')
    obj = request.files.get('file_obj')
    key = 'app_static/oms/test/img/' + file_name
    oss_task(key, obj.read())  # # 直接读取文件内容并传递 否则可能出现 ValueError: I/O operation on closed file. 异常
    return jsonify(code="200", message="success", data={"img_name": file_name, 'img_key': key})


if __name__ == '__main__':
    app.run()
