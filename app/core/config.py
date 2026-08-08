
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus #trata a senha com caracteres especiais


load_dotenv() #le o arquivo env


DB_HOST = os.getenv ("DB_HOST") #pega uma variavel do ambiente
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

#codifica a senha para nao quebrar a url
raw_password = os.getenv("DB_PASSWORD")
DB_PASSWORD = quote_plus(raw_password) if raw_password else "" 
