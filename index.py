import sqlite3
conn = sqlite3.connect('UserData.db')
tableName = 'User'
c = conn.cursor()

#region DB Control
def checkTableReady():
    sqlstr = "SELECT name FROM sqlite_master WHERE type='table' AND name='{table}';".format(table = tableName)
    c.execute(sqlstr)
    result = c.fetchone()
    if result == None:
        sqlstr = "CREATE TABLE {table} (id int, name text, birthday text, createTime text);".format(table = tableName)
        c.execute(sqlstr)

def getMaxId():
    maxId = 0
    sqlstr = "SELECT max(id) FROM {table};".format(table = tableName)
    c.execute(sqlstr)
    result = c.fetchone()
    if len(result) > 0:
        if result[0] == None:
            return 0
        else:
            return int(result[0])
    return maxId

def select_All():
    sqlstr = "SELECT * FROM {table};".format(table = tableName)
    c.execute(sqlstr)
    return c.fetchall()

def select_By_ID(id):
    sqlstr = "SELECT * FROM {table} WHERE id = ?;".format(table = tableName)
    c.execute(sqlstr, str(id))
    return c.fetchone()

def insert(name, birthday):
    sqlstr = "INSERT INTO {table} VALUES (?, ?, ?, date('now'))".format(table = tableName)
    c.execute(sqlstr, (getMaxId() + 1, name, birthday))
    conn.commit()

def update(id, name, birthday):
    sqlstr = "UPDATE {table} SET name = ?, birthday = ? WHERE id = ?;".format(table = tableName)
    c.execute(sqlstr, (name, birthday, id))
    return c.fetchone()

def delete(id):
    sqlstr = "DELETE FROM {table} WHERE id = ?;".format(table = tableName)
    c.execute(sqlstr, str(id))
    conn.commit()
#endregion

checkTableReady()

#insert("test", "2000-01-01")

#update(2, "test2", "2001-01-01")

#delete(2)

#selectResult = select_By_ID(3)
selectResult = select_All()
print(selectResult)

conn.close()