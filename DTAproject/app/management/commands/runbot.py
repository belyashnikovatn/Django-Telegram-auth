from telebot import TeleBot

from django.core.management.base import BaseCommand

from DTAproject.settings import BOT_TOKEN
from app.models import User


class Command(BaseCommand):
    help = 'Run your Telegram-bot'

    async def handle(self, *args, **options):
        """Make a bot and start work."""

        bot = TeleBot(token=BOT_TOKEN)

        @bot.message_handler(commands=['start', 'hi'])
        def start_up(message):
            chat_id = message.chat.id
            name = message.chat.first_name
            User.objects.get_or_create(
                tlg_id=chat_id,
                tlg_name=name
            )
            bot.send_message(chat_id, text=f'User {name} created!')

        bot.infinity_polling()