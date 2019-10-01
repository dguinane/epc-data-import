import os

EPC_LOGIN_URL = 'https://epc.opendatacommunities.org/login-with-token'
EPC_CERT_LOCATION = 'https://epc.opendatacommunities.org/files/all-domestic-certificates.zip'
EPC_LOCAL_LOCATION = 'data/epc.zip'
EPC_SELECTED_COLS = ['LMK_KEY', 'LODGEMENT_DATE', 'TRANSACTION_TYPE', 'TOTAL_FLOOR_AREA', 'ADDRESS', 'POSTCODE']
DB_CONFIG = {
    'db_user': os.environ['DB_USER'],
    'db_pass': os.environ['DB_PASS'],
    'db_host': os.environ['DB_HOST']
}
EPC_PK = 'LMK_KEY'
