import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('pizza_cool.db')
    cur = base.cursor()
    if base:
        print('Подключена база данных')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy as data:
        base.commit()
    # async with state.proxy as data:
    #     pass
        # print(data.values())
        # cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        # base.commit()
