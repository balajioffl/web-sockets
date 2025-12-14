from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(user_logged_in)
def notify_login(sender, request, user, **kwargs):
    channel_layer = get_channel_layer()
    message = f"{user.username} just logged in!"
    async_to_sync(channel_layer.group_send)(
        "notifications",
        {
            "type": "send_notification",
            "message": message
        }
    )
