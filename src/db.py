import sqlalchemy
from const import DB_CONFIG, EPC_PK
import logging


def setup_db():
    with sqlalchemy.create_engine('postgresql+psycopg2://{db_user}:{db_pass}@{db_host}'
                                          .format(**DB_CONFIG)).connect() as conn:
        logging.info('DB connected, creating table')
        conn.execute("""
        CREATE TABLE IF NOT EXISTS epc_records (
              LMK_KEY bigint,
              LODGEMENT_DATE date,
              TRANSACTION_TYPE text,
              TOTAL_FLOOR_AREA float,
              ADDRESS text,
              POSTCOST text
        )""")


def insert_df(df):
    with sqlalchemy.create_engine('postgresql+psycopg2://{db_user}:{db_pass}@{db_host}'
                                          .format(**DB_CONFIG)).connect() as conn:
        insert_statement = conn.insert('epc_records').values(df.to_dict(orient='records'))
        upsert_statement = insert_statement.on_conflict_do_update(
            index_elements=[EPC_PK],
            set_={c.key: c for c in insert_statement.excluded if c.key != EPC_PK})
        conn.execute(upsert_statement)
