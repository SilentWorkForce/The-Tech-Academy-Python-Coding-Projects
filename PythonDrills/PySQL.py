

import sqlite3

conn = sqlite3.connect('Drill.db')

with conn:
     cur = conn.cursor()
     cur.execute("CREATE TABLE IF NOT EXISTS tbl_project(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fileName TEXT, \
            col_fileType TEXT \
            )")
     conn.commit()
conn.close()


conn = sqlite3.connect('Drill.db')

with conn:
    cur = conn.cursor()
    cur.execute('insert into tbl_project(col_fileName, col_fileType) values(?,?)', \
                ('Hello','.txt'))
    cur.execute('insert into tbl_project(col_fileName, col_fileType) values(?,?)', \
                ('myImage','.png'))
    cur.execute('insert into tbl_project(col_fileName, col_fileType) values(?,?)', \
                ('myMovie','.mpg'))
    cur.execute('insert into tbl_project(col_fileName, col_fileType) values(?,?)', \
                ('World','.txt'))
    cur.execute('insert into tbl_project(col_fileName, col_fileType) values(?,?)', \
                ('Data','.pdf'))
    cur.execute('insert into tbl_project(col_fileName, col_fileType) values(?,?)', \
                ('myPhoto','.jpg'))
    conn.commit()
conn.close()


conn = sqlite3.connect('Drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("select col_fileName,col_fileType FROM tbl_project WHERE col_fileType = '.txt'")
    varProject = cur.fetchall()
    for item in varProject:
        msg = 'File Name: {}\nFile Type: {}'.format(item[0],item[1])
    print(msg)

