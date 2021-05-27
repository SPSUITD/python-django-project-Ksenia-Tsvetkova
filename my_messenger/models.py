from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Chat(models.Model):
  name=models.CharField(max_length=100)

class Message(models.Model):
  body=models.CharField(max_length=400)
  sender=models.CharField(max_length=200)
  chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
  created_at=models.DateTimeField(auto_now_add=True)
