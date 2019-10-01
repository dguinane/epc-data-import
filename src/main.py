from const import EPC_CERT_LOCATION, EPC_LOCAL_LOCATION, EPC_SELECTED_COLS
from lib import get_epc_sess, get_epc_dfs
from db import insert_df, setup_db
from log import setup_logging
import logging


def fetch_epc_data():
    sess = get_epc_sess()
    res = sess.get(EPC_CERT_LOCATION,
                   stream=True)
    logging.info('Logged in to EPC website, downloading feed')
    with open(EPC_LOCAL_LOCATION, 'wb') as f:
        for chunk in res.iter_content(chunk_size=1024):
            f.write(chunk)
    logging.info('Finished feed download')


def write_data():
    for _df in get_epc_dfs(EPC_LOCAL_LOCATION):
        df = _df[EPC_SELECTED_COLS]
        insert_df(df)


def main():
    setup_logging()
    logging.info('Starting DB setup')
    setup_db()
    logging.info('Fetching EPC data')
    fetch_epc_data()
    logging.info('Writing EPC data to DB')
    write_data()


if __name__ == '__main__':
    main()
