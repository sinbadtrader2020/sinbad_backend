from flask import Flask, request
from flask.json import JSONEncoder
from flask_restful import Api
from flask_cors import CORS
from functools import wraps
from datetime import date

from src.api.signin import signin
from src.api.signup import signup
from src.api.subscribe_user import subscribe_user
from src.api.get_app_url import get_app_url_user
from src.utils import pmemcached
from src.api.apilist import apis
from src.config import ApiConfig
from src.mail.mailing import set_config


pmemcachedapi = None


# Source: https://stackoverflow.com/a/43663918
#         http://flask.pocoo.org/snippets/119/
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Hello decorator")
        print(len(args), " ", args)
        print(len(kwargs), " ", kwargs)
        print(request.headers.get(ApiConfig.TOKEN))

        request.headers.get(ApiConfig.TOKEN)
        # print(request.headers)
        return func(*args, **kwargs)
    return wrapper


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)
    app.json_encoder = CustomJSONEncoder

    app.config.update(
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_TLS=False,
        MAIL_USE_SSL=True,
        MAIL_USERNAME='marufcuet007@gmail.com',
        MAIL_PASSWORD='lhvrqebkcjhatcuz'
    )

    set_config(app)

    # try:
    #     from flask_debugtoolbar import DebugToolbarExtension
    #     DebugToolbarExtension(app)
    # except:
    #     pass

    api = Api(app=app, prefix='{prefix}/v{version}'.format(prefix=app.config['REST_URL_PREFIX'],
                                                           version=app.config['API_VERSION']),
              decorators=[authenticate])

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    for key, value in apis.items():
        api.add_resource(value, key)

    pmemcachedapi = pmemcached.connectmemcached()

    signin(app)
    signup(app)
    subscribe_user(app)
    get_app_url_user(app)

    return app