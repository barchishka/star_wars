from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv('DB_NAME', 'swapi')
DB_USER = os.getenv('DB_USER', 'swapi')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'secret')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

DSN = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
