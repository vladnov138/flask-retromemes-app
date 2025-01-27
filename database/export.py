import sqlite3
import sqlite3 as sl

users = ['id', 'login', 'password', 'avatar']
post = ['id', 'author_id', 'text', 'image', 'date', 'like', 'dislike']
rates = ['post_id', 'real_likes', 'real_dislikes']

DB_root = ['users', 'post', 'rates']
DB = [users, post, rates]

con = sl.connect('memes.db')
with con:
    data = con.execute('SELECT * FROM users')
    for row in data:
        print(row)
    print('----------')
    data1 = con.execute('SELECT * FROM users WHERE id == 1')
    for row in data1:
        print(row)
