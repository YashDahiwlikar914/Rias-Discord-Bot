# Rias - Discord Assistant Bot

Rias is a Discord bot that works as a personal assistant with an actual personality. It uses Google's Generative AI API to handle conversations, maintains history so responses stay contextually relevant, and can be tuned for different roles and conversational styles.

## Features

- **Conversational AI** using Google Generative AI for natural language responses
- **Conversation history** stored in `History.json` for contextual awareness across messages
- **Multi-channel support** across text channels and DMs
- **Trigger recognition** via mentions, replies, DMs, and configurable keywords

## Getting Started

### Prerequisites

- Python 3.7+
- Google Generative AI API key
- Discord bot token

### Installation

1. Clone the repo

```bash
git clone git@github.com:YashDahiwlikar914/Rias-Discord-Bot.git
cd Rias-Discord-Bot
```

2. Install dependencies

```bash
pip install discord google-generativeai
```

3. Set up your keys

Replace `API_KEY` in the code with your Google Generative AI key, and `DISCORD_TOKEN` with your bot token from the [Discord Developer Portal](https://discord.com/developers/applications).

4. Run the bot

```bash
python Main.py
```

## Configuration

### Generative AI Settings

Tune these in `generation_config`:

| Parameter | What it controls |
|---|---|
| `temperature` | Creativity. Lower = more deterministic, higher = more random. |
| `top_p` | Probability distribution for response diversity. |
| `top_k` | How many top tokens are considered per step. |
| `max_output_tokens` | Hard cap on response length. |

### Personality

Edit `system_instruction` to change how Rias talks and what role it plays. This is where the personality lives.

### History

Conversation history is in `History.json`. Clear it if you want a fresh context, or let it persist across restarts. Your call.

## Usage

Once running, the console will show `Logged On As {Bot Name}!` on successful connection.

Rias responds when you mention it, reply to one of its messages, or DM it. Custom trigger words can be added in the message filter section of the code.

**Example:**
```
User: @Rias How's the weather?
Rias: I'm not a meteorologist, but I can tell you it'll be sunny whenever you're around! 😏
```

## Troubleshooting

**Bot not responding** - Check that `API_KEY` and `DISCORD_TOKEN` are valid. Also verify that `message_content` intent is enabled in both the code and the Discord Developer Portal.

**API error** - Confirm your key has Generative AI permissions and you haven't hit your quota. If you're close to limits, reduce `max_output_tokens`.

**JSON decode error on `History.json`** - The file is probably malformed. Clear it or delete it. The bot recreates it automatically.

## Contributing

1. Fork the project
2. Create a feature branch: `git checkout -b feature/feature-name`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push: `git push origin feature/feature-name`
5. Open a Pull Request

## License

MIT License.
