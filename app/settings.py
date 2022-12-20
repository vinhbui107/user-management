import os

from dotenv import load_dotenv

ENV = os.getenv("ENV")

if (ENV is not None or ENV == 'dev') and os.path.exists('config/' + ENV + '.env'):
    load_dotenv('config/' + ENV + '.env')
else:
    load_dotenv()

# DB connection
DB_DIALECT = "postgresql"
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# SendGird configuration
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDGRID_ADMIN_EMAIL = os.getenv("SENDGRID_ADMIN_EMAIL")

# Redis connection
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_DB = os.getenv("REDIS_DB")
