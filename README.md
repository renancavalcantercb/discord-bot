# Discord.py bot

This is a discord bot made using discord.py lib

## Configuration
Before running the bot, you need to create a `.env` file with your OpenAI API credentials. To do this, create a file called `.env` in the project root and add the following:
```
TOKEN=your_discord_bot_token_here
OPENAI_API_KEY=your_open_api_key_here
```
Replace `your_discord_bot_token_here` and `your_api_key_here` with your discord bot token and OpenAI API token.

## Installation
To install the project dependencies, run the following command:
```python
pip install -r requirements.txt
```

## Execution
To run the bot, run the following command:
```python
python bot.py
```

## Commands
The following commands are available:
- `hello`:  Responds with a simple "Hello!" message.
- `create_service`: It creates a service form that is filled in as the user answers questions, it is used for clue services in Runescape 3.
- `clear <value>`: Deletes text messages based on the value you pass as a parameter. This command can be useful for cleaning up cluttered channels or removing unwanted messages.

## Tree Commands
The following tree commands are available:
- `/gpt <question>`: Sends the question to the OpenAI API and returns a response. This command is used to interact with the ChatGPT model and ask questions or get advice on various topics.

## Roadmap
The following features are planned for future releases:
- Improve user interface in gpt command response
- Add integration with youtube and spotify to play music

## Contributing
Contributions are welcome! If you have an idea for a feature or would like to contribute a bug fix or improvement, feel free to submit a pull request.
