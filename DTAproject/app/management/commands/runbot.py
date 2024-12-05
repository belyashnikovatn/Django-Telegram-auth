from telebot import TeleBot, types

from django.core.management.base import BaseCommand
from django.shortcuts import redirect

from DTAproject.settings import BOT_TOKEN
from app.models import User


class Command(BaseCommand):
    help = 'Run your Telegram-bot'

    def handle(self, *args, **options):
        """Make a bot and start work."""

        bot = TeleBot(token=BOT_TOKEN)

        @bot.message_handler(commands=['start'])
        def start(message):
            tlg_id = message.chat.id
            name = message.chat.first_name
            user = User.objects.get_or_create(
                tlg_id=tlg_id,
                tlg_name=name
            )
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("click", url=f'127.0.0.1:8000/homepage/{tlg_id}')
            markup.add(button1)
            bot.send_message(message.chat.id, "на сайт", reply_markup=markup)

        bot.polling(none_stop=True)
