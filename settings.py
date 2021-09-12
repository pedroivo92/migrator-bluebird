import os

CONTAINER_NUMBER = os.getenv('CONTAINER_NUMBER')

DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_CONNECTION_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

GLOBOMAIL_DB_USER = os.getenv('GLOBOMAIL_DB_USER')
GLOBOMAIL_DB_PASSWORD = os.getenv('GLOBOMAIL_DB_PASSWORD')
GLOBOMAIL_DB_HOST = os.getenv('GLOBOMAIL_DB_HOST')
GLOBOMAIL_DB_NAME = os.getenv('GLOBOMAIL_DB_NAME')

ROUNDCUBE_DB_USER = os.getenv('ROUNDCUBE_DB_USER')
ROUNDCUBE_DB_PASSWORD = os.getenv('ROUNDCUBE_DB_PASSWORD')
ROUNDCUBE_DB_HOST = os.getenv('ROUNDCUBE_DB_HOST')
ROUNDCUBE_DB_NAME = os.getenv('ROUNDCUBE_DB_NAME')

AUTH_USER = os.getenv('AUTH_USER')
AUTH_USER_AKAKO = os.getenv('AUTH_USER_AKAKO')
AUTH_PASSWORD = os.getenv('AUTH_PASSWORD')
AUTH_PASSWORD_AKAKO = os.getenv('AUTH_PASSWORD_AKAKO')
AUTH_URL = os.getenv('AUTH_URL')
AUTH_URL_AKAKO = os.getenv('AUTH_URL_AKAKO')
AUTH_SERVICE_CAPI = os.getenv('AUTH_SERVICE_CAPI')
AUTH_SERVICE_BLUEBIRD = os.getenv('AUTH_SERVICE_BLUEBIRD')
AUTH_SERVICE_AKAKO = os.getenv('AUTH_SERVICE_AKAKO')
AUTH_SERVICE_NOTIFICATION = os.getenv('AUTH_SERVICE_NOTIFICATION')

CAPI_URL = os.getenv('CAPI_URL')
BLUEBIRD_URL = os.getenv('BLUEBIRD_URL')
AKAKO_URL = os.getenv('AKAKO_URL')
NOTIFICATION_URL = os.getenv('NOTIFICATION_URL')


CAPI_TIMEOUT = os.getenv('CAPI_TIMEOUT')
PAYMENT_TIMEOUT = os.getenv('PAYMENT_TIMEOUT')
CART_TIMEOUT = os.getenv('CART_TIMEOUT')
CHECKOUT_TIMEOUT = os.getenv('CHECKOUT_TIMEOUT')
AUTH_TIMEOUT = os.getenv('AUTH_TIMEOUT')
AKAKO_TIMEOUT = os.getenv('AKAKO_TIMEOUT')
NOTIFICATION_TIMEOUT = os.getenv('NOTIFICATION_TIMEOUT')
DATABASE_CONNECTION_TIMEOUT = os.getenv('DATABASE_CONNECTION_TIMEOUT')
APPLICATION_SECRETS = os.getenv('APPLICATION_SECRETS')