import MySQLdb
import os


def create_dbs(names):
    django_settings = __import__(os.environ['DJANGO_SETTINGS_MODULE'], fromlist='DATABASES')
    databases = django_settings.DATABASES
    for name, db in databases.iteritems():
        if name in names and db['ENGINE'].endswith('mysql'):
            host = db['HOST']
            user = db['USER']
            password = db['PASSWORD']
            port = db['PORT']
            db_name = db['NAME']
            print 'creating database %s on %s' % (db_name, host)
            db = MySQLdb.connect(user=user,
                                passwd=password,
                                host=host,
                                port=port)
            cur = db.cursor()
            print("Check if database is already there.")
            cur.execute("""SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA 
                         WHERE SCHEMA_NAME = %s""", (db_name,))
            results = cur.fetchone()
            if not results:
                print("Database %s doesn't exist, lets create it." % db_name)
                sql = """CREATE DATABASE IF NOT EXISTS %s """ % (db_name,)
                print("> %s" % sql)
                cur.execute(sql)
                print(".....")
            else:
                print("database already exists, moving on to next step.")


if __name__ == '__main__':
    import sys
    create_dbs(sys.argv[1:])