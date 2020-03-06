import os

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.urandom(12).hex()
    FLASK_ENV = os.getenv("FLASK_ENV")


class DevelopmentConfig(BaseConfig):
    """
    Development configurations
    """


class ProductionConfig(BaseConfig):
    pass


class LocalConfig(BaseConfig):
    """
    Production configurations
    """


def get_config():
    app_env = {"dev": DevelopmentConfig,
               "prod": ProductionConfig,
               "local": LocalConfig}
    return app_env[os.getenv('FLASK_ENV')]