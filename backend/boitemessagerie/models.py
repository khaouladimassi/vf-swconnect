from django.db import models
from accounts.models import CustomUser
from django.core.exceptions import ValidationError

class Messagerie(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='messages/files/', blank=True, null=True)
    seen=models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender} to {self.receiver} at {self.timestamp}'

    def save(self, *args, **kwargs):
        if not self.body and not self.file:
            raise ValidationError("Either body or file must be provided")
        super().save(*args, **kwargs)