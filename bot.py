from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio, os, random

api_id = 24751547
api_hash = "a125209289c5281b43a67d02019aa97f"

chat_id = -1003621946413
session = os.getenv("SESSION")

client = TelegramClient(StringSession(session), api_id, api_hash)

async def main():
    await client.start()
    print("24/7 auto /grow started")

    while True:
        try:
            await client.send_message(chat_id, "/grow")
            delay = random.randint(180, 240)
            await asyncio.sleep(delay)
        except Exception as e:
            print(e)
            await asyncio.sleep(120)

client.loop.run_until_complete(main())
