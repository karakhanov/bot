from .models import Client, UserTelegram, Orders


def user_func(update):
    try:
        user = UserTelegram.objects.get(id_telegram=update.effective_user.id)
    except:
        user = UserTelegram(id_telegram=update.effective_user.id, username=update.effective_user.username, bed=1,
                            baby=0, pet=0, breakfast=0, lan='uz')
        user.save()
    return user


def client_func(update, user):
    try:
        client = Client.objects.get(telegram_user_id=update.effective_user.id)
    except:
        client = Client(telegram_user_id=update.effective_user.id, state=Client.STATE_FULLNAME, user_info=user)
        client.save()
    return client

def do_order(client):
    newOrder = Orders(telegram_user_id=client.telegram_user_id,
                      room_class=client.room_class,
                      bed=client.user_info.bed,
                      baby=client.user_info.baby,
                      pet=client.user_info.pet,
                      breakfast=client.user_info.breakfast,
                      fullName=client.fullName,
                      phone=client.phone,
                      email=client.email,
                      is_firm=client.is_firm,
                      country=client.country,
                      start_date=client.start_date,
                      finish_date=client.finish_date)
    newOrder.save()