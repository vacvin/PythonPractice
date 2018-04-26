import sqlite3
global conn
global tableName
global tableFieldDefine

tableFieldDefine = {
    'User' : {
        'Define' : 'id int, name text, birthday text, createTime text',
        'Insert' : '?, ?, ?, date(\'now\')',
        'Update' : 'name = ?, birthday = ? WHERE id = ?'
    }
}

#region DB Control
def checkTableReady():
    sqlstr = "SELECT name FROM sqlite_master WHERE type='table' AND name='{table}';".format(table = tableName)
    c = conn.cursor()
    c.execute(sqlstr)
    result = c.fetchone()
    if result == None:     
        sqlstr = "CREATE TABLE {table} ({fields}});".format(table = tableName, fields = tableFieldDefine[tableName]['Define'])
        c.execute(sqlstr)

def getMaxId():
    checkTableReady()
    maxId = 0
    sqlstr = "SELECT max(id) FROM {table};".format(table = tableName)
    c = conn.cursor()
    c.execute(sqlstr)
    result = c.fetchone()
    if len(result) > 0:
        if result[0] == None:
            return 0
        else:
            return int(result[0])
    return maxId

def select_All():
    checkTableReady()
    sqlstr = "SELECT * FROM {table};".format(table = tableName)
    c = conn.cursor()
    c.execute(sqlstr)
    return c.fetchall()

def select_By_ID(id):
    checkTableReady()
    sqlstr = "SELECT * FROM {table} WHERE id = ?;".format(table = tableName)
    c = conn.cursor()
    c.execute(sqlstr, str(id))
    return c.fetchone()

def insert(values):
    checkTableReady()    
    sqlstr = "INSERT INTO {table} VALUES ({fields})".format(table = tableName, fields = tableFieldDefine[tableName]['Insert'])
    c = conn.cursor()
    c.execute(sqlstr, (getMaxId() + 1,) + tuple(values))
    conn.commit()
    return c.lastrowid

def update(id, values):
    checkTableReady()
    sqlstr = "UPDATE {table} SET {fields};".format(table = tableName, fields = tableFieldDefine[tableName]['Update'])
    c = conn.cursor()
    c.execute(sqlstr, tuple(values) + (id,))
    conn.commit()
    return c.fetchone()

def delete(id):
    checkTableReady()
    sqlstr = "DELETE FROM {table} WHERE id = ?;".format(table = tableName)
    c = conn.cursor()
    c.execute(sqlstr, str(id))
    conn.commit()

def DBConnect(DBName, _tableName):
    global conn 
    global tableName
    conn = sqlite3.connect(DBName)
    tableName = _tableName

def DBClose():
    conn.close()
#endregion


