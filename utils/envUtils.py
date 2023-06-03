from dotenv import load_dotenv
import os

load_dotenv()

class ENVIRONMENT:
    TOKEN = os.environ["TOKEN"]
    APPNAME = os.environ["APPNAME"]
    SQUARE_APP_ID_SANDBOX = os.environ["SQUARE_APP_ID_SANDBOX"]
    SQUARE_TOKEN_SANDBOX = os.environ["SQUARE_TOKEN_SANDBOX"]
    PAYMENT_PROVIDER_TOKEN = os.environ["PAYMENT_PROVIDER_TOKEN"]
    
ENV = ENVIRONMENT()
