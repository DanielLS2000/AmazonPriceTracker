import sqlite3
from Produto import Produto
from datetime import datetime

if __name__ == '__main__':
    conn = sqlite3.connect('producttracker.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE produtos_rastreados(name TEXT, price FLOAT, rating TEXT, data DATE)''')
    c.execute('''CREATE TABLE produtos_recentes(name TEXT PRIMARY KEY, price FLOAT, rating TEXT)''')
