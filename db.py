import mysql.connector
import mysql.connector.pooling
from mysql.connector import errorcode

local_config = {
    'user': 'root',
    'password': 'root-password',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'edu_latest',
    'raise_on_warnings': True,
}

localpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "localpool",
                                                      pool_size = 32,
                                                      **local_config)

def get_local_connection():
    return localpool.get_connection()

def handleError(err):
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("LOCAL DB: Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("LOCAL DB: Database does not exist")
    else:
        print("LOCAL DB: " + str(err))

def escape(str):
    #print "~~ " + str
    string =  str.strip().replace("'", "\'").replace("\"", "\\\"").replace(")", "\)").replace("(", "\(")
    #print "== " + ugh
    return string