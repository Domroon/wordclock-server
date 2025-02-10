import configparser
from pathlib import Path

from flask import Flask

PATH = Path().cwd()
CONFIG_PATH = PATH / 'config' / 'config.ini'

app = Flask(__name__)

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

infos = config['infos']
version_folder = f'v{infos["version"].replace('.', '')}'
data_link = f'{infos["domain_name"]}/{infos["subsite_name"]}/{version_folder }/{infos["filename"]}'
filenames = ["main.py", "test_1.py", "test_2.py"]


@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route('/version')
def latest_version():
    return config['infos']['version']

@app.route('/link')
def link():
    return data_link

@app.route('/version-info')
def version_info():
    return {
        "link": f'{infos["domain_name"]}/{infos["subsite_name"]}/{version_folder }/{infos["filename"]}',
        "filenames": filenames
    }


if __name__ == "__main__":
    app.run(debug=True)