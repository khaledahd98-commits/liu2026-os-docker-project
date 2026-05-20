from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'db'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', 'root_password_fst'),
            database=os.getenv('DB_NAME', 'liu_db')
        )
        cursor = conn.cursor()
        cursor.execute('SELECT NOW()')
        now = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return f'<h1>Docker Web + MySQL Stack</h1><p>Database connected successfully.</p><p>DB time: {now}</p>'
    except Exception as e:
        return f'<h1>Docker Web + MySQL Stack</h1><p>Database connection error: {e}</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
