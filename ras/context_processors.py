import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render
from mysql.connector import Error
import pymysql
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')



def __get_temper_neryngri():
    temper_query = (f"SELECT real_value tmp FROM charts_real WHERE context_id = 6 ORDER BY id DESC LIMIT 1")
    connection_temper = create_connection('ip', 'user', 'password', 'db_name', 3306)
    tempers = execute_read_query(connection_temper, temper_query)
    tempers__ = [list(x) for x in tempers]
    temper_ = tempers__[0]
    temper_neryngri = temper_[0]
    return temper_neryngri


def __get_temper_chulman():
    temper_query = (f"SELECT real_value tmp FROM charts_real WHERE context_id = 63 ORDER BY id DESC LIMIT 1")
    connection_temper = create_connection('ip', 'user', 'password', 'db_name', 3306)
    tempers = execute_read_query(connection_temper, temper_query)
    tempers__ = [list(x) for x in tempers]
    temper_ = tempers__[0]
    temper_chulman = temper_[0]
    return temper_chulman


def base(request):
    temper_neryngri = __get_temper_neryngri()
    temper_chulman = __get_temper_chulman()



    return {
        'temper_neryngri': temper_neryngri,
        'temper_chulman': temper_chulman,
    }


def update_temper_and_date(request):
    temper_neryngri = __get_temper_neryngri()
    temper_chulman = __get_temper_chulman()
    date_now = datetime.datetime.now().strftime("%d %B %Y г.")
    data_dict = {
        'temper_neryngri': float(temper_neryngri),
        'temper_chulman': float(temper_chulman),
        'date_now': str(date_now)
    }
    return HttpResponse(json.dumps(data_dict))


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
    cursor.close()


def create_connection(host_name, user_name, user_password, db_name, name_port):
    connection = None
    try:
        connection = pymysql.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name,
            port=name_port
        )

    except Error as e:
        print(f"Произошла ошибка: {e}")
    return connection
