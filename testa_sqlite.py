import sqlite3
try:
    conn = sqlite3.connect('licitacoes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT sqlite_version();')
    result = cursor.fetchall()
    print(f'result {result}')
    cursor.close()
except sqlite3.Error as error:
    print(f'Error: {error}')
finally:
    if conn:
        conn.close()