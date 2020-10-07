import sqlite3
from datetime import datetime
conn = sqlite3.connect(
    'C:\\Users\\Bevan\\Desktop\\New folder (3)\\myflaskapp\\flaskblog\\site.db')

c = conn.cursor()
#c.execute("DROP TABLE employee")

# c.execute("""CREATE TABLE employee(
#                id INTEGER,
#                qid INTEGER NOT NULL,
#                pid INTEGER NOT NULL,
#                answer01 VARCHAR(500),
#                answer02 VARCHAR(500),
#                answer03 VARCHAR(500),
#                answer04 VARCHAR(500),
#                answer05 VARCHAR(500),
#                date_posted DATETIME NOT NULL,
#                user_id INTEGER NOT NULL,
#                PRIMARY KEY (id),
#                FOREIGN KEY(user_id) REFERENCES user(id))""")

c.execute("""UPDATE employee SET answer01 = :answer01, date_posted = :date_posted
            WHERE id = :id AND qid = :qid AND pid = :pid AND user_id = :user_id """,
          {'answer01': 'mytexsdadasadsdadasddasdasdt', 'id': 1, 'qid': 1, 'pid': 1, 'user_id': 1, 'date_posted': datetime.now()})
c.execute("""UPDATE employee SET answer03 = :answer01, date_posted = :date_posted
            WHERE id = :id AND qid = :qid AND pid = :pid AND user_id = :user_id """,
          {'answer01': 'i like to kiss you', 'id': 1, 'qid': 1, 'pid': 1, 'user_id': 1, 'date_posted': datetime.now()})
# c.execute("INSERT INTO employee(id, qid, pid, date_posted, user_id) VALUES(?, ?, ?, ?,?)",
#          (2, 1, 1, datetime.now(), 1))

conn.commit()


#c.execute("SELECT * FROM employee WHERE last='Schafer'")

# print(c.fetchall())

# c.execute("""UPDATE employee SET speaks.qid = 1 WHERE AND""")

conn.close()
