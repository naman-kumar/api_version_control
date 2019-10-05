import functools
from flask import abort
from flask import Flask
from flask import request


app = Flask(__name__)


def api_v1():
    return "This is api version v1"


def api_v1_1():
    return "This is api version v1_1"


def api_v1_2():
    return "This is api version v1_2"


def api_v2(msg):
    return msg


def api_v3():
    return "This is api version v3"


def api_v4():
    return "This is api version v4"


def api_version_control(**kwargs):
    def outer(func):
        @functools.wraps(func)
        def inner():
            v = request.args.get('v')
            if not v:
                return func()
            method_version = kwargs.get(v)
            if isinstance(method_version, tuple):
                method = method_version[0]
                args = method_version[1:]
                return method(*args)
            elif method_version:
                return method_version()
            else:
                return abort(404)
        return inner
    return outer


@app.route('/')
@api_version_control(
    v1=api_v1,
    v1_1=api_v1_1,
    v1_2=api_v1_2,
    v2=(api_v2, 'Hello world from api version v2'),
    v3=api_v3,
    v4=api_v4
)
def index():
    return "Hello world!"


if __name__ == "__main__":
    app.run(debug=True,port=5000)

