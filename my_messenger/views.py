from django.shortcuts import render, redirect, get_object_or_404

from .models import Message, Chat

def index(request):
  username=request.session.get('username')
  if not username:
    return redirect('get_username')

  chats=Chat.objects.all()
  return render(request, 'index.html', {'chats': chats})

def get_username(request):
  if request.method == 'POST':
    username=request.POST.get('username')
    request.session.update({'username':username})
    return redirect('index')
  
  return render(request, 'username_form.html')

def chat_page(request, name):
  chat = get_object_or_404(Chat, name=name)
  username=request.session.get('username')
  if request.method == 'POST':
    msg = Message(
      body=request.POST.get('body'),
      sender=username,
      chat=chat
    )
    msg.save()
  
  messages = Message.objects.filter(chat=chat).order_by('created_at')
  return render(request, 'chat_page.html', {'messages': messages, 'chat': chat})