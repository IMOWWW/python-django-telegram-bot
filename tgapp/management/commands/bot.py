from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.utils.request import Request
from tgapp.models import Profile, Message, MessageMe

from datetime import time
 


def log_errors(f):

    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'An error has occurred: {e}'
            print(error_message)
            raise e

    return inner


@log_errors
def do_echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text

    p, _ = Profile.objects.get_or_create(
        user_id=chat_id,
        defaults={
            'username': update.message.from_user.username,
            'f_name': update.message.from_user.first_name,
            'l_name': update.message.from_user.last_name,
        }
    )

    m = MessageMe(
        profile=p,
        messages=text,
    )
    m.save()

    reply_text = f'Your ID = {chat_id}\n{text}'
    # reply_text = f'Добро пожаловать!'
    update.message.reply_text(
        text=reply_text,
    )


@log_errors
def start_do(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text

    p, _ = Profile.objects.get_or_create(
        user_id=chat_id,
        defaults={
            'username': update.message.from_user.username,
            'f_name': update.message.from_user.first_name,
            'l_name': update.message.from_user.last_name,
        }
    )
    # m = Message(
    #     profile=p,
    #     text=text,
    # )
    # m.save()

    # reply_text = f'Ваш ID = {chat_id}\n{text}'
    reply_text = f'Добро пожаловать в бот!'
    update.message.reply_text(
        text=reply_text,
    )


@log_errors
def send_message_bot(context: CallbackContext):
    users = Profile.objects.all()
    for i in users:
        user_id = Profile.objects.get(pk=i)
        message_test = Message.objects.get()
        context.bot.send_message(user_id.user_id, message_test.text)


class Command(BaseCommand):
    help = "TG BOT на django"

    def handle(self, *args, **options):
        # 1 -- правильное подключение
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
            base_url=getattr(settings, 'PROXY_URL', None),
        )
        print(bot.get_me())

        # 2 -- обработчики
        updater = Updater(
            bot=bot,
            use_context=True,
        )




        command_handler = CommandHandler("start", start_do)
        message_handler = MessageHandler(Filters.text, do_echo)
        updater.dispatcher.add_handler(command_handler)
        updater.dispatcher.add_handler(message_handler)
        updater.job_queue.run_daily(send_message_bot, time(hour=2, minute=0, second=0, microsecond=0),days=[0,1,2,3,4,5,6])

        # 3 -- запустить бесконечную обработку входящих сообщений
        updater.start_polling()
        updater.idle()


    

