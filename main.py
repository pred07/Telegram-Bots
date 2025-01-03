from typing import Final
from telegram import Update
from telegram.ext import Application, StringCommandHandler, MessageHandler, CommandHandler, filters, ContextTypes

TOKEN: Final = 'token'
BOT_USERNAME = '@bot_name'

#commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Welcome to the club ! I am assistant bot')
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Type something, so I can respond !')
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is custom command !')
  
#Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()
    print(f"Processing message: {processed}")

    if 'hello' in processed:
        return 'Hey there!'
    if 'how are you' in processed:
        return 'I am good! How about you?'
    
    return 'I do not understand...'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat_id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))


    #Error
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval = 3)
