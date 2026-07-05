# Rias Discord bot
**This project is outdated and no longer maintained. I don't work on it anymore. The code stays up for reference, but it might break as APIs and dependencies change.** <br>

Rias is a Discord bot built to act like a personal assistant with a real personality. It uses Google's Generative AI API to chat. It saves conversation history so it remembers what you were talking about, and you can tune it for different roles and styles.

## What it does

The bot handles natural language responses through the Google Generative AI API. It stores past messages in `History.json` to keep context active across the conversation. It works in both standard text channels and direct messages. You can trigger it by mentioning it, replying to one of its messages, sending a DM, or using specific keywords.

## Setup

You need Python 3.7 or newer. You also need an API key from Google Generative AI and a bot token from the Discord Developer Portal.

First, clone the repository and move into the directory.

```bash
git clone git@github.com:YashDahiwlikar914/Rias-Discord-Bot.git
cd Rias-Discord-Bot
```

Install the required packages.

```bash
pip install discord google-generativeai
```

Open the code and swap out the placeholders. Put your Google Generative AI key in place of `API_KEY`. Put your Discord bot token in place of `DISCORD_TOKEN`.

Start the bot.

```bash
python Main.py
```

## Configuration

You can change how the AI generates text by editing `generation_config`. 

| Parameter | What it controls |
|---|---|
| `temperature` | Low means predictable. High means random. |
| `top_p` | Controls response diversity. |
| `top_k` | Sets how many top tokens the model looks at per step. |
| `max_output_tokens` | Sets a hard limit on response length. |

To change the bot's personality, edit `system_instruction`. This controls how Rias talks and what role it plays. 

The bot saves conversation context in `History.json`. You can clear this file to start fresh or leave it alone to keep history across restarts.

## Usage

When the bot connects, the console prints a message confirming it logged on.

Rias answers when you mention it, reply to it, or send a DM. You can add custom trigger words to the message filter section in the code.

```text
User: @Rias How's the weather?
Rias: I'm not a meteorologist, but I can tell you it'll be sunny whenever you're around! 😏
```

## Troubleshooting

If the bot isn't responding, check your API key and Discord token. Make sure the `message_content` intent is enabled in your code and in the Discord Developer Portal.

If you get an API error, check your Google Generative AI permissions. Make sure you haven't hit your quota. If you are close to the limit, try lowering `max_output_tokens`.

If you see a JSON decode error for `History.json`, the file is probably broken. Delete it. The bot will make a new one automatically.

## License

This project uses the MIT License.
