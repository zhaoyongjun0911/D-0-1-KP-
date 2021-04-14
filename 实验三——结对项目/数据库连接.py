config = {
    'host': 'localhost',
    'port': 3307,
    'user': 'root',
    'password': '815490',
    'db': 'dk',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}

connection = pymysql.connect(**config)
connection.autocommit(True)
cursor = connection.cursor()

def get_table_list():
    results=[]
    cursor.execute('show tables from dk;')
    query_result = cursor.fetchall()
    for i in query_result:
        results.append(i['Tables_in_dk'])
    return results

def get_data(sets_name):
    sql='select * from '+sets_name+';'
    cursor.execute(sql)
    query_result = cursor.fetchall()
    return query_result