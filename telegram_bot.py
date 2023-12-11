
from typing import final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes,CallbackContext
#replace this with your bot token
TOKEN:final='Your bot Token'

#replcae this with your bot username
BOT_USERNAME: final='Your bot UserName'


# A hypothetical movie database (movie_name: download_link)
movie_database = {
    "extraordinaryman": "https://t.me/c/1665557397/6949",
    "hinana": "https://t.me/c/1665557397/6890",
    # Add more movies and links as needed
}

async def start_command(update:Update,Context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(' Hello!  iam bot ')
async def help_command(update:Update,Context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! please send your problem')
async def custom_command(update:Update,Context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')

def handle_response(text:str) -> str:
    processed :str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'
    if 'how are you' in processed:
        return 'hello'
    if 'i love you' in processed:
        return 'love you too'
    if processed in movie_database:
        return f'{processed} : {movie_database[processed]}'


    return 'i dont understand what are you talking'







async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    message_type:str = update.message.chat.type
    text:str=update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}:"{text}"')


    if message_type =='group':
        if BOT_USERNAME in text:
            new_text:str =text.removesuffix(BOT_USERNAME,'').strip()
            response:str=handle_response(new_text)
        else:
            return
    else:
        response:str=handle_response(text)

    print('BOT:',response)
    await update.message.reply_text(response)




async def error(update:Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'update {update} caused error {context.error}')

if __name__ == '__main__':
    print('startinf bot...')

    app=Application.builder().token(TOKEN).build()


    #commands

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))


    #messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))




    #errors

    app.add_error_handler(error)


    #polls the bot
    print('polling...')
    app.run_polling(poll_interval=3)
