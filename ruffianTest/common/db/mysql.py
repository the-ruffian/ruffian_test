import pymysql


class Mysql:
    def __init__(self, host, user, password, database=None, charset="utf8"):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)  # 得到一个可以执行SQL语句的光标对象 结果返回字典 默认元祖

    def close_db(self):
        self.cursor.close()

    def data_operation(self, sql, data='', operation='select'):
        """

        :param sql:
        :param data: Usually used when inserting data; [(),(),...]
                    when there is no data，（sql, '', operation）
        :param operation: default is select
        :return:
        """
        if data == '':
            if operation != 'select':
                self.cursor.execute(sql)
                self.conn.commit()
                self.cursor.close()
            else:
                self.cursor.execute(sql)
                results = self.cursor.fetchall()
                self.cursor.close()
                return results
        elif data != '':
            self.cursor.executemany(sql, data)
            self.conn.commit()
            self.cursor.close()

    def database_and_table_operation(self, statements):
        '''
        :param statements: your sql statements
        '''
        self.cursor.execute(statements)
'''
    Example 1
    s = Mysql('host', 'user', 'pwd', 'database')
    s1 = s.data_operation('select * from user', '', 'select')
    print(s1)

    Example 2
    s = Mysql('host', 'user', 'pwd', 'database')
    data = [
        ('july', '147'),
        ('june', '258'),
        ('marin', '369')
    ]
    s1 = s.data_operation('insert into userinfo(user,pwd) values(%s,%s)', data)
    
    # Example 3  database and table operation
    s = Mysql('host', 'user', 'pwd')
    s.database_and_table_operation('create database if not exists test')
    s.database_and_table_operation('use test')
    s.database_and_table_operation('create table if not exists userinfo(user varchar(20),pwd varchar(20))')
    s.conn.close()
    '''
