import random, tracemalloc, asyncio
from telethon import TelegramClient, events

api_id = #
api_hash = '#'
bot_token = '1945950955:#'

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('/spin me right round baby right round like a record baby right rounnddd roundd roundddd')
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='/list'))
async def start(event):
    chat = await event.get_chat()
    chat_id = event.chat_id
    users = await bot.get_participants(chat)
    for user in users:
        if user.username is not None:
            await event.respond(user.first_name)
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/spin'))
async def start(event):
    chat = await event.get_chat()
    users = await bot.get_participants(chat)
    luckywinner = random.choice(users)
    await event.respond('congratulations my nigga,' + ' @' + luckywinner.username + '.')

def main():
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
