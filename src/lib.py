import os
import requests
import pandas
from zipfile import ZipFile
from const import EPC_LOGIN_URL


def get_epc_sess():
    sess = requests.session()
    sess.get(EPC_LOGIN_URL, params={'token': os.environ['LOGIN_TOKEN'],
                                    'email': os.environ['LOGIN_EMAIL']})
    return sess


def get_epc_dfs(location):
    with ZipFile(location, 'r') as zarc:
        for zf in zarc.infolist():
            if 'certificates.csv' in zf.filename:
                with zarc.open(zf.filename) as f:
                    df = pandas.read_csv(f)
                    yield df
