import aiosqlite
import os
import logging

DB_PATH = os.path.join(os.path.dirname(__file__), '../../assets/bot.db')

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            channel TEXT,
            source TEXT,
            post_id TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')
        await db.commit()
    logging.info("Database initialized.")

async def log_post(channel: str, source: str, post_id: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('INSERT INTO posts (channel, source, post_id) VALUES (?, ?, ?)', (channel, source, post_id))
        await db.commit()

async def get_recent_posts(channel: str, limit: int = 50):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute('SELECT * FROM posts WHERE channel = ? ORDER BY timestamp DESC LIMIT ?', (channel, limit)) as cursor:
            return await cursor.fetchall()
