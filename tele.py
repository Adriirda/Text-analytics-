
import asyncio
from datetime import datetime, timedelta
from telethon import TelegramClient, events
import pandas as pd
import nltk

# Replace the values with your own API ID, API hash, and phone number
api_id = "28356764"
api_hash = '1b5d29e0db4898319da49090cald307'
phone_number = '+601163200308'

group_name = -1001462876169   # Replace with your group ID
# enter your channel group id -100 after this digit

# Set the time range to get messages from
start_time = datetime.now() - timedelta(hours=24)
flag = 0

async def get_group_messages():
    df = pd.DataFrame({'Data': [''], 'name': [''], 'mobile': ['']})
    df1 = pd.DataFrame({'Data': [''], 'name': [''], 'mobile': ['']})
     # Create a Telegram client with the specified API ID, API hash and phone number
    client = TelegramClient('session_name', api_id, api_hash)
    await client.connect()
    
    # Check if the user is already authorized, otherwise prompt the user to authorize the client
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Enter the code: '))

    # Get the ID of the specified group
    group = await client.get_entity(group_name)
    date_today = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    
    yesterday = date_today - timedelta(days=5)
    messages = []
     # below commented code is used for  specified time range
    async for message in client.iter_messages(group, min_id=1):
        print(message.date, yesterday)
        if str(message.date) < str(yesterday):
            break
        messages.append(message)
        
asyncio.run(get_group_messages())