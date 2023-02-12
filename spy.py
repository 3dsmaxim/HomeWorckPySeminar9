from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


def log(update: Update, context: ContextTypes):
    file = open('db.csv', 'a')
    file.writelines(f'{update.effective_user.first_name}\n')
    file.writelines(f'{update.effective_user.id}\n')
    file.writelines(f'{update.message.text}\n')
    file.close()
