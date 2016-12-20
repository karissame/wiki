import mysql.connector
import config

class Page:
    content = "No one has added content for this topic yet. Feel free to edit this page now!!"
    def __init__(self,title):
        self.title = title
        self.author = ""
        self.id=0
        self.last_modified = ""
        #make sure this works then escape characters in content, title
        query = "SELECT id, title, content, last_modified, author FROM page where title='%s'" %title
        entry = Database.getResult(query,True)
        if not entry is None:
            self.content = entry[2]
            self.last_modified = entry[3]
            self.author = entry[4]
            self.id = entry[0]
        # print "content is %s" % self.content

    def getContent(self):
        return self.content

    def save(self):
        if self.id >0:
            return self.update()
        else:
            return self.insert()
    def insert(self):
        query = "INSERT into page (title,content,author) values ('%s','%s','%s')" % (self.title,self.content,self.author)
        self.id=Database.doQuery(query)
        return self.id
        # lastId=cur.lastrowid

    def update(self):
        query = "UPDATE page set content='%s',author='%s' WHERE title = '%s'" % (self.content,self.author,self.title)
        Database.doQuery(query)
        return True

    def delete(self):
        query = ("UPDATE page set deleted=1 where title=%s"%self.title)
        Database.doQuery(query)
        return True

    def __str__(self):
     return self.title

    @staticmethod
    def getObjects():
        query = "SELECT title FROM page where deleted=0"
        result_set = Database.getResult(query)
        allpages=[]
        for item in result_set:
            title = item[0]
            allpages.append(Page(title))
        return allpages

class Database:
    @staticmethod
    def getConnection():
        return mysql.connector.connect(user=config.dbUser,password=config.dbPass,host=config.dbHost,database=config.dbName)
    @staticmethod
    def escape(value):
        return value.replace("'","''")
    @staticmethod
    def getResult(query,getOne=False):
        conn = Database.getConnection()
        cur = conn.cursor()
        cur.execute(query)
        if getOne:
            result_set = cur.fetchone()
        else:
            result_set = cur.fetchall()
        cur.close()
        conn.close()
        return result_set
    @staticmethod
    def doQuery(query):
        conn = Database.getConnection()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        lastId = cur.lastrowid
        cur.close()
        conn.close()
        return lastId
