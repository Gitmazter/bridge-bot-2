from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import Constants as keys
import responses as R
import asyncio
from api import endpoint


# Commands
async def start_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text('Hello \n I have been expecting you... \n Type something to get started!')
  
async def help_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text('Ever heard of Google?')

async def custom_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("This is a custom command!")

# Responses
async def handle_message(update : Update, context : ContextTypes.DEFAULT_TYPE):
  text:str = update.message.text
  
  # debug
  print(f'User: ({update.message.chat.id}) sent "{text}')

  response: str = R.sample_responses(text)
  
  # debug
  print("Bot: ", response)
  await update.message.reply_text(response)

# error handler
async def error(update : Update, context : ContextTypes.DEFAULT_TYPE):
  print(f"Update {update} caused error {context.error}")


async def sendIt (app) :
  await app.bot.send_message(chat_id='-4030149233', text='Ayyyy')

def main():
  print("I have arisen!")
  # Commands
  api = endpoint()
  endpoint.start(api)

  app = Application.builder().token(keys.API_KEY).build()


  app.add_handler(CommandHandler("start", start_command))
  app.add_handler(CommandHandler("help", help_command))
  app.add_handler(CommandHandler("custom", custom_command))

  # Handle Message
  app.add_handler(MessageHandler(filters.TEXT, handle_message))
  
  # Handle Error
  app.add_error_handler(error)

  # Polling Messages
  print("Polling...")

  app.run_polling(poll_interval=3)

main()
