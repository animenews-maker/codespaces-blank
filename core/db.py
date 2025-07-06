import aiosqlite
import asyncio

DB_PATH = "animebot.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS posted (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT,
                item_id TEXT,
                channel_id TEXT,
                posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        await db.commit()

def run_init_db():
    asyncio.run(init_db())
