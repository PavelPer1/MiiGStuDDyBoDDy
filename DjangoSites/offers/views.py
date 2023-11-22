import json

from django.shortcuts import render
from django.utils.safestring import mark_safe

from users.models import HelpMe, Profile
from .models import CreateOffers, ChatMessage
from django.core.mail import send_mail, EmailMessage
from Mysite import settings


def page_offer(request, offer):
    inform_offer = HelpMe.objects.get(id=offer)
    users_profile = Profile.objects.get(user_id=inform_offer.user_id)

    if 'response' in request.POST:
        user = request.user.id
        user_offer = inform_offer.user_id
        his_offer = inform_offer

        of = CreateOffers(
            user_id=user,
            user_offer_id=user_offer,
            offer=his_offer
        )

        of.save()
        data = f"""
        Привет на твою запись откликнулся {request.user.username}
        Заходи на сайт и начинай заниматься!!!!
                ((()))((()))
                    (())
        """
        email = EmailMessage(
            subject='Отклик',
            body=data,
            from_email='mstuddybuddy@mail.ru',
            to=[users_profile.email]
        )
        email.send()

    context = {
        'inform_offer': inform_offer,
        'users_profile': users_profile
    }

    return render(request, 'page_offer.html', context)


def get_my_offers(request):
    my_offers = CreateOffers.objects.filter(user_offer_id=request.user.id)

    context = {
        'my_offers': my_offers
    }

    return render(request, 'my_offers.html', context)


def room_view(request, room_name):
    all_message = ChatMessage.objects.filter(room_name=room_name)

    return render(request, 'room.html', {
        'room_name': room_name,
        'all_message': all_message
    })


