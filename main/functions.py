from .models import Client, UserTelegram


def user_func(update):
    try:
        user = UserTelegram.objects.get(id_telegram=update.effective_user.id)
    except:
        user = UserTelegram(id_telegram=update.effective_user.id, username=update.effective_user.username, bed=1,
                            baby=0, pet=0, breakfast=0, lan='uz')
        user.save()
    return user


def client_func(update):
    try:
        client = Client.objects.get(telegram_user_id=update.effective_user.id)
    except:
        client = Client(telegram_user_id=update.effective_user.id, state=Client.STATE_FULLNAME)
        client.save()
    return client
