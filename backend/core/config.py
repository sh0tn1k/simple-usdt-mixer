import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME: str = "SQB Mixer"
    PROJECT_VERSION: str = "0.1"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    # default postgres port is 5432
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "mega_db")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY :str = os.getenv("SECRET_KEY")
    ALGORITHM :str = os.getenv("ALGORITHM")

    SUBSCRIBE = 1 # в месяцах

    DEBUG_CHECK_PASSWORD = True     # TODO Comment out for release deployment

    # TRON Network Access
    TRONGRID_API_KEY = "cf0f2ea3-839e-41b3-b5d4-bab491e08432"
    TRON_NETWORK = "Sashta"  # default TRC20
    COMMISSION = 0.2
    # TRON_ADDRESS
    TRON_ADDRESS: str = os.getenv("TRON_ADDRESS")
    TRON_ADDRESS_PRIV_KEY: str = os.getenv("TRON_ADDRESS_PRIV_KEY")

    # Debug parameters
    DBG_SKIP_TRANSACTIONS_POLLING = os.getenv("DBG_SKIP_TRANSACTIONS_POLLING")

settings = Settings()