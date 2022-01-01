import sqlite3
db = sqlite3.connect('jam.db')
cursor =db.cursor()

# Delete account
def delete_account():
    enter_memID = input('enter member id: ')
    cursor.execute('DELETE * FROM MEMBER WHERE MID = ?',(enter_memID))
    db.commit()
    

# login
def login():
    enter_memID = input('enter member id: ')
    cursor.execute('SELECT * FROM MEMBER WHERE MID = ?',(enter_memID))
    db.commit()
 