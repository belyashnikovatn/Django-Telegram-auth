from telebot import TeleBot, types

from django.core.management.base import BaseCommand
from django.shortcuts import redirect

from DTAproject.settings import BOT_TOKEN, DOMAIN
from app.models import User


class Command(BaseCommand):
    help = 'Run your Telegram-bot'

    def handle(self, *args, **options):
        """Make a bot and start work."""

        bot = TeleBot(token=BOT_TOKEN)

        @bot.message_handler(commands=['start'])
        def start(message):
            """Create a user if doesnt exist."""
            tlg_id = message.chat.id
            name = message.chat.first_name
            User.objects.get_or_create(
                tlg_id=tlg_id,
                tlg_name=name
            )
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("на сайт", url=f'http://{DOMAIN}/homepage/{tlg_id}')
            markup.add(button1)
            bot.send_message(message.chat.id, "Вернуться", reply_markup=markup)

        bot.polling(none_stop=True)
