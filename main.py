import pyodbc
db_server = 'sql-server-aiagents.database.windows.net'
database = 'db_aiagents'
username = 'aiagent-admin'
password = 'A!agent01'
driver = '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+db_server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password) as conn:
    with conn.cursor() as cursor:
        cursor.execute('''
                        CREATE TABLE test1(
                            id int primary key,
                            name nvarchar(50),
                            price int
                        )
        ''')
        consor.commit()