import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='todo_db'
    )

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            deadline DATE,
            status ENUM("pending", "processing", "cancelled", "done") DEFAULT "pending"  
        )
    """)
    conn.commit()
    conn.close()
