from django.shortcuts import render
from django.views import View

from chat.forms import MessageForm
from chat.models import Chat, Message


def get_dialogs(request):
    chats = []
    for i in Chat.objects.all():
        if i.user1_id == request.user.id or i.user2_id == request.user.id:
            chats += [i]

    context = {
        'user_profile': request.user,
        'chats': chats,
    }
    return render(request, 'dialogs.html', context)
"""if 'send' in request.POST and request.method == 'POST':
        print('1111')
        mes = request.POST.get('message')

        mess = Message(
            chat_id=num,
            author=request.user.id,
            message=mes,
        )

        mess.save()"""


def dialogs_views(request, num):
    message = Message.objects.filter(chat_id=num)
    submitbutton = request.POST.get("submit")
    form = MessageForm(request.POST or None)

    mes = ''

    if form.is_valid():
        mes = form.cleaned_data.get('message')
        mess = Message(
            chat_id=num,
            author_id=request.user.id,
            message=mes,
        )

        mess.save()
    context = {
        'form': form,
        'message': message
    }

    return render(request, 'chat.html', context)



