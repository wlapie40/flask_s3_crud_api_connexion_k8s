from flask import render_template
import connexion
import logging
import os
from config.config import get_config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

CUR_ENV = str(os.environ['FLASK_ENV'])
logging.info(f'cur_env: {CUR_ENV}')

config = get_config()

app = connexion.App(__name__, specification_dir="api/")

app.add_api('swagger.yml')


if __name__ == '__main__':
    app.run(port=8080, debug=True)
