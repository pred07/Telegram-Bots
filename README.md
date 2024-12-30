Telegram Bot Setup and Deployment on PythonAnywhere

1. Create a Bot Using BotFather
Open Telegram and search for BotFather.
Start a chat and use the following commands:
/newbot – Create a new bot.
Provide a name for your bot (e.g., "MyAssistantBot").
Provide a username (must end with bot, e.g., my_assistant_bot).
BotFather will generate a Token (e.g., 123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11).
Save this token securely. It will be used in your Python script.
2. Write the Bot Script
Install the python-telegram-bot library:
 
Copy code
pip install python-telegram-bot
Create a Python script (main.py):
python
Copy code
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = 'YOUR_BOT_TOKEN'
BOT_USERNAME = '@your_bot_username'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Welcome to the bot.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Type something, so I can respond!')

def handle_response(text: str) -> str:
    processed = text.lower()
    if 'hello' in processed:
        return 'Hey there!'
    if 'how are you' in processed:
        return 'I am good! How about you?'
    return 'I do not understand...'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    response = handle_response(text)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error)

    app.run_polling()
3. Test the Script Locally
Run the script:
 
Copy code
python main.py
Test the bot by sending /start or /help commands on Telegram.
4. Deploy the Bot on PythonAnywhere
Sign Up/Log In at PythonAnywhere.

Upload Your Script:

Go to the "Files" section.
Upload main.py and any dependencies.
Install Dependencies:

Open a Bash console on PythonAnywhere.
Install python-telegram-bot:
pip install --user python-telegram-bot
Run the Script:

Open a Bash console and run:
python main.py