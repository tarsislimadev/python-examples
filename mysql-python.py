# docker run -d --name mysql1 -e MYSQL_DATABASE=mysql1 -e MYSQL_ROOT_PASSWORD=pwd1 -p 3306:3306 mysql

# # 

# python -m pip install mysql-connector-python

import mysql.connector

# Establish connection
conn = mysql.connector.connect(host='localhost', user='root', password='pwd1', database='mysql1')

# Create a cursor object
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  age INT
)
''')

cursor.execute('INSERT INTO users (name, age) VALUES (%s, %s)', ('Alice', 25))
conn.commit()

cursor.execute('SELECT * FROM users')
results = cursor.fetchall()

for row in results:
  print('Row: ', row)

cursor.execute('UPDATE users SET age = %s WHERE name = %s', (30, 'Alice'))
conn.commit()

# cursor.execute('DELETE FROM users WHERE name = %s', ('Alice',))
# conn.commit()

cursor.close()
conn.close()
