import sqlite3
db = sqlite3.connect('tasks_db')
cursor = db.cursor()
#cursor.execute('''CREATE TABLE Tasks(id INTEGER PRIMARY KEY , task TEXT , priority TEXT , date TEXT)''')
def tasks_input(task,pr,dt):
    cursor.execute('''INSERT INTO Tasks(task,priority,date) VALUES(?,?,?)''', (task,pr,dt))
    cursor.execute('''SELECT task,priority,date FROM Tasks''')
    data1 = cursor.fetchall()
    db.commit()
def import_db():
    cursor.execute('''SELECT task,priority,date FROM Tasks''')
    data2 = cursor.fetchall()
    db.commit()
    return data2
def tasks_delete(task1):
    cursor.execute('''DELETE FROM Tasks WHERE task = ? ''',(task1[0],))
    db.commit()
def tasks_update(task2,task3,pr1,dt1):
    cursor.execute('''UPDATE Tasks SET task = ? WHERE task = ?''' , (task3,task2))
    cursor.execute('''UPDATE Tasks SET date = ? WHERE task = ?''', (dt1, task3))
    cursor.execute('''UPDATE Tasks SET priority = ? WHERE task = ?''', (pr1, task3))
