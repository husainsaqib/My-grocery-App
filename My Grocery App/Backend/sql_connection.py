from typing import Any

import mysql.connector

__cnx=None

def get_sql_connection() -> Any:
    """

    :rtype: PooledMySQLConnection | MySQLConnectionAbstract
    """
    global __cnx
    if __cnx is None:
        __cnx=mysql.connector.connect(user='root', password='Mosaqi@1234',
                                  host='127.0.0.1',
                                  database='gs')

    return __cnx