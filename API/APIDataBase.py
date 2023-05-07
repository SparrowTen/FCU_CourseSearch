import pymysql
from dbutils.pooled_db import PooledDB

class APIDataBase:
    def __init__(self, host, port, user, database):
        self.POOL = PooledDB(
            creator = pymysql,    
            maxconnections = 6,   # 最大連線數
            mincached = 2,        # 最小初始創建的連線數
            maxcached = 5,        # 最大閒置連線數
            maxshared = 3,        # 連線最高數
            blocking = True,      # 連線中如果沒有可用連線是否卡等待
            maxusage = None,      # 一個連線最多被重複使用的次數
            
            host = host,
            port = port,
            user = user,
            # password='',
            database = database,
            charset = 'utf8'
        )
    
    def execSelect(self, sql):
        conn = self.POOL.connection()
        cursor = conn.cursor()
        resault = cursor.execute(sql)
        resault = cursor.fetchall()
        data = []
        column_names = [desc[0] for desc in cursor.description]
        for row in resault:
            row_with_column_names = dict(zip(column_names, row))
            data.append(row_with_column_names)
        conn.close()
        return data

    def exec(self, sql):
        conn = self.POOL.connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

# 測試用
# if __name__ == '__main__':
#     db = APIDataBase('localhost', 3306, 'root', 'fcu')
#     sql = 'SELECT * FROM `1111_course`'
#     data = db.exec(sql)
#     print(data)