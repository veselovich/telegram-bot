import sqlite3 as sq

async def db_start():
    global db, cur

    db = sq.connect('profiles.db')
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS profiles(
                user_id TEXT PRIMATY KEY,
                name TEXT,
                age TEXT,
                photo TEXT,
                description TEXT
                )
    """)
    
    db.commit()

async def create_profile(user_id):
    user = cur.execute("SELECT 1 FROM profiles WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO profiles VALUES(?, ?, ?, ?, ?)", (user_id, '', '', '', ''))
        db.commit()


async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cur.execute("UPDATE profiles SET name = '{}', age = '{}', photo = '{}', description = '{}' WHERE user_id == '{}';".format(
            data['name'], data['age'], data['photo'], data['description'], user_id))
        db.commit()