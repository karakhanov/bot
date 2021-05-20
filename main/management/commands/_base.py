from telegram.ext import Updater
from django.core.management.base import BaseCommand


class BotBase(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(BotBase, self).__init__(*args, **kwargs)


        self.updater = Updater("987901929:AAGXNZRYYet3z_fqYRNbjilLsPJHZJwBHbg")