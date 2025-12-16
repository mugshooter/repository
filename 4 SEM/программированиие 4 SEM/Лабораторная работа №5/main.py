import functools
import sys
from typing import Union, TextIO
import json
import sqlite3
from datetime import datetime
from collections import Counter

FILE = 'logdata.json'

def trace(func=None, *, handle=sys.stdout):

    if func is None:
        return lambda func: trace(func, handle=handle)

    if handle == 'fp':
        log_data = []

    elif handle == 'db':
        connection = sqlite3.connect(":memory:")
        cursor = connection.cursor()
        try:
            cursor.execute('CREATE TABLE logs (datetime TEXT, func_name TEXT, params TEXT, result TEXT)')
        except sqlite3.OperationalError as e:
            print(f"Error creating table: {e}")

    @functools.wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)

        log_entry = {
            'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'func_name': f'{func.__name__}()',
            'params': args,
            'result': result
        }

        if handle == sys.stdout:
            print(log_entry)
        elif handle == 'logdata':
            with open(FILE, 'a') as fp:
                json.dump([log_entry], fp, indent=2)
                fp.write('\n')
        elif handle == 'fp':
            log_data.append(log_entry)
        elif handle == 'db':
            try:
                cursor.execute('INSERT INTO logs VALUES (?, ?, ?, ?)',
                               (log_entry['datetime'], log_entry['func_name'], json.dumps(log_entry['params']),
                                str(log_entry['result'])))
                connection.commit()
            except sqlite3.OperationalError as e:
                print(f"Error inserting into logs table: {e}")

        return result

    if handle == 'fp':
        def save_logs_to_file():
            with open(FILE, 'a') as fp:
                for log_entry in log_data:
                    json.dump([log_entry], fp, indent=2)
                    fp.write('\n')

        inner.save_logs_to_file = save_logs_to_file

    return inner


def sql3_util_printer():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    try:
        cursor.execute('CREATE TABLE logs (datetime TEXT, func_name TEXT, params TEXT, result TEXT)')
    except sqlite3.OperationalError as e:
        print(f"Error creating table: {e}")
    cursor.execute('SELECT * FROM logs')
    logs = cursor.fetchall()

    for log in logs:
        print({
            'datetime': log[0],
            'func_name': log[1],
            'params': json.loads(log[2]) if log[2] else None,
            'result': log[3]
        })


@trace
def f1(args: Union[list, tuple]) -> int:
    return sum(args)

fp = TextIO()
@trace(handle='fp')
def f2(text: str) -> str:
    return text[::-1]

db = sqlite3.connect(":memory:")
@trace(handle='db')
def f3(data: list) -> dict:
    counter = Counter(data)
    return dict(counter)

f1([1, 2, 3, 4, 5, 6])
f1((1, 2, 3, 4, 5, 6))

f2('GOTOVO')

f3([1, 2, 3, 1, 2, 3, 4, 5])

f2.save_logs_to_file()

sql3_util_printer()

db.close()