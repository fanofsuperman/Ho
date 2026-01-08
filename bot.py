from telethon import TelegramClient
import asyncio

api_id = 24751547
api_hash = "a125209289c5281b43a67d02019aa97f"

chat_id = -1003621946413  # CHANGE THIS to your target channel/group ID

client = TelegramClient("grow_session", api_id, api_hash)

async def main():
    await client.start()
    print("Logged in. Auto /grow started.")

    while True:
        try:
            await client.send_message(chat_id, "/grow")
            print("Sent /grow")
            await asyncio.sleep(30)
        except Exception as e:
            print("Error:", e)
            await asyncio.sleep(60)

client.loop.run_until_complete(main())
