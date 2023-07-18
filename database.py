import sqlite3 as sq
import random

async def db_start():
    global db, cur
    db = sq.connect('profiles.db')
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS profiles(
                user_id TEXT PRIMATY KEY,
                username TEXT,
                name TEXT,
                age TEXT,
                photo TEXT,
                description TEXT
                )
    """)

    db.commit()

async def create_profile(user_id, username):
    user = cur.execute("SELECT 1 FROM profiles WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO profiles VALUES(?, ?, ?, ?, ?, ?)", (user_id, username, '', '', '', ''))
        db.commit()


async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cur.execute("UPDATE profiles SET name = '{}', age = '{}', photo = '{}', description = '{}' WHERE user_id == '{}';".format(
            data['name'], data['age'], data['photo'], data['description'], user_id))
        db.commit()


async def get_rnd_profile():
    db.row_factory = sq.Row
    cur = db.cursor()
    cur.execute("SELECT * FROM profiles;")
    rows_as_dict = cur.fetchall()
    global get_profile
    try:
        get_profile_tmp = get_profile
    except NameError:
        get_profile = {}
        get_profile_tmp = {}
    while True:
        get_profile = random.choice(rows_as_dict)
        if get_profile != get_profile_tmp:
            break
    return get_profile

async def db_end():
    cur.close()
    db.close()