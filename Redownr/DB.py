import sqlite3
import time

SCHEMA = {
    "users":
        "\n\t" +
        "id         integer primary key autoincrement, \n\t" +
        "username   text unique, \n\t" +
        "sinceid    text, \n\t" +
        "created    integer, \n\t",
    "images":
        "\n\t" +
        "id     integer primary key autoincrement, \n\t" +
        "path   text unique, \n\t" +
        "userid integer, \n\t" +
        "url    text, \n\t" +
        "created    integer, \n\t" +
        "foreign key(userid) references users(id) \n\t" 
}

class DB(object):
    """description of class"""
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        if SCHEMA != None and SCHEMA != {} and len(SCHEMA) > 0:
            for key in SCHEMA:
                self.create_table(key, SCHEMA[key])

    def create_table(self, table_name, schema):
        cur = self.conn.cursor()
        query = '''create table if not exists %s (%s)''' % (table_name, schema)
        cur.execute(query)
        self.commit()
        cur.close()

    def commit(self):
        try_again = True
        while try_again:
            try:
                self.conn.commit()
                try_again = False
            except:
                time.sleep(1)

    def add_user(self, user):
        cur = self.conn.cursor()
        now = time.time()
        q = "insert into users values ("
        q += "NULL,"                        #id
        q += "'%s',"    % user.user_name    #username
        q += "'',"                          #sinceid
        q+= "'%s'"      % now               #created
        try:
            cur.execute(q)
        except sqlite3.IntegrityError as e:
            print("add_user: user '%s' already exists in db" % user.user_name)
            raise e
        self.commit()