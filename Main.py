import discord
import os
import json
import google.generativeai as genai
from discord.message import Message

# API Configurations
API_KEY = "GEMINI_API_KEY"
HISTORY_FILE = "History.json"
DISCORD_TOKEN = 'BOT_TOKEN'

# Generative AI Model Configuration
genai.configure(api_key=API_KEY)
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
# noinspection PyTypeChecker
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=("Enter Your Description Of Bot"),
)


# Helper Functions for History
def load_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_history(history):
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


# Initialize history and chat session
history = load_history()
chat_session = model.start_chat(history=history)


# Discord Bot Class
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged On As {self.user}!')

    async def on_message(self, message):
        # Ignore bot's own messages
        if message.author == self.user:
            return

        # Check if bot was mentioned or replied to
        bot_mentioned = self.user in message.mentions
        bot_replied = (
                message.reference
                and isinstance(message.reference.resolved, Message)
                and message.reference.resolved.author == self.user
        )
        is_dm = isinstance(message.channel, discord.DMChannel)

        # Check if message needs a response from Rias
        if "rias" in message.content.lower() or bot_replied or bot_mentioned or is_dm:
            user_message = {"role": "user", "parts": [{"text": message.content}]}
            history.append(user_message)

            # Generate response
            response = chat_session.send_message(message.content)
            bot_response = {"role": "model", "parts": [{"text": response.text}]}
            history.append(bot_response)
            save_history(history)

            # Send response
            await message.channel.send(response.text)

        # Log message to console
        print(f'Message From {message.author}: {message.content}')


# Initialize and run client
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(DISCORD_TOKEN)
